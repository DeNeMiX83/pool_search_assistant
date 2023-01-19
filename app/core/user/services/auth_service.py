import uuid
from dataclasses import asdict

from app.core.user.exceptions.user import UserAlreadyExistsException

from app.core.user.protocols.hasher_password import HasherPassword
from app.core.user.protocols.jwt_service import JwtService
from app.core.user.protocols.auth_sevice import AuthService

from app.core.user.protocols.dao.session_write import UserSessionWriteDao
from app.core.user.protocols.dao.user_write import UserWriteDao
from app.core.user.protocols.dao.user_read import UserReadDao

from app.core.user.entities import value_objects as vo
from app.core.user import entities
from app.core.user import dto

from app.core.user.exceptions.user import UserNotFoundError, InvalidPasswordError

class AuthServiceImp(AuthService):

    def __init__(
        self,
        hasher_password: HasherPassword,
        jwt_service: JwtService,
        dao_user_session: UserSessionWriteDao,
        dao_user_write: UserWriteDao,
        dao_user_read: UserReadDao
    ):
        self._hasher_password = hasher_password
        self._jwt_service = jwt_service
        self._dao_user_session = dao_user_session
        self._dao_user_write = dao_user_write
        self._dao_user_read = dao_user_read

    async def register(self, user: dto.User) -> None:
        email = user.email
        username = user.username
        password = user.password

        hashed_password = self._hasher_password.hash(password)
        user = entities.User(
            email=vo.Email(email),
            username=vo.UserName(username),
            hashed_password=vo.HashedPassword(hashed_password)
        )
        
        await self._dao_user_write.create(user)
        await self._dao_user_write.commit()

    async def login(self, user: dto.UserLogin) -> int:
        user_entity = await self._dao_user_read.get_by_email(user.email)

        if not user_entity:
            raise UserNotFoundError()

        if not self._hasher_password.verify_password(user.password, user_entity.hashed_password):
            raise InvalidPasswordError()

        session_id = uuid.uuid4()
        jwt_token = self._jwt_service.encode(user.dict())
        
        session_dto = dto.SessionWrite(
            session_id=session_id,
            jwt_token=jwt_token
        )

        await self._dao_user_session.create(session_dto)

        return session_id

    async def logout(self, session_id: int) -> None:
        self._dao_user_session.delete(session_id)


    
