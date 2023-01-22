import uuid

from app.core.user.protocols.hasher_password import HasherPassword
from app.core.user.protocols.jwt_service import JwtService
from app.core.user.protocols.auth_sevice import AuthService

from app.core.user.protocols.dao.user_session_write import UserSessionWriteDao
from app.core.user.protocols.dao.user_session_read import UserSessionReadDao
from app.core.user.protocols.dao.user_write import UserWriteDao
from app.core.user.protocols.dao.user_read import UserReadDao
from app.core.shared.protocols import Committer

from app.core.user.entities import value_objects as vo
from app.core.user import entities
from app.core.user import dto

from sqlalchemy.exc import IntegrityError
from app.core.user.exceptions import AuthError


class AuthServiceImp(AuthService):
    def __init__(
        self,
        hasher_password: HasherPassword,
        jwt_service: JwtService,
        dao_user_session_write: UserSessionWriteDao,
        dao_user_session_read: UserSessionReadDao,
        dao_user_write: UserWriteDao,
        dao_user_read: UserReadDao,
        committer: Committer,
    ):
        self._hasher_password = hasher_password
        self._jwt_service = jwt_service
        self._dao_user_session_write = dao_user_session_write
        self._dao_user_session_read = dao_user_session_read
        self._dao_user_write = dao_user_write
        self._dao_user_read = dao_user_read
        self._committer = committer

    async def register(self, user: dto.UserRegister) -> None:
        email = user.email
        username = user.username
        raw_password = user.raw_password

        try:
            raw_password = vo.RawPassword(raw_password)
            hashed_password = self._hasher_password.hash(raw_password.value)

            user = entities.User(
                email=vo.Email(email),
                username=vo.UserName(username),
                hashed_password=vo.HashedPassword(hashed_password),
            )
        except ValueError as e:
            raise AuthError(e)
        except TypeError as e:
            raise AuthError(e)

        try:
            await self._dao_user_write.create(user)
            await self._committer.commit()
        except IntegrityError:
            await self._committer.rollback()
            raise AuthError("user already exists")

    async def login(self, user: dto.UserLogin) -> int:
        user_entity = await self._dao_user_read.get_by_email(user.email)

        if not user_entity:
            raise AuthError("user not found")
        if not self._hasher_password.verify_password(
            user.password, user_entity.hashed_password
        ):
            raise AuthError("invalid password")

        session_id = uuid.uuid4()
        jwt_token = self._jwt_service.encode({"user_id": str(user_entity.id)})

        session_dto = dto.SessionWrite(
            session_id=session_id, jwt_token=jwt_token
        )

        await self._dao_user_session_write.create(session_dto)

        return session_id

    async def logout(self, user: dto.UserLogout) -> None:
        session_id = user.session_id
        try:
            await self._dao_user_session_read.get(session_id)
        except ValueError as e:
            raise AuthError(e)
        await self._dao_user_session_write.delete(session_id)
