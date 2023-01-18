from sqlalchemy.exc import IntegrityError

from app.core.user import entities
from app.core.user.entities import value_objects as vo

from app.core.shared.usecase.usecase import UseCase
from app.core.user.protocols.dao.user_write import UserWrite
from app.core.user import dto
from app.core.user.exceptions.user import UserAlreadyExistsException

from app.core.user.protocols.hasher_password import HasherPassword

class RegisterUserUseCase(UseCase):
    def __init__(
        self, 
        dao: UserWrite, 
        hasher: HasherPassword
    ):
        self._dao = dao
        self._hasher = hasher

    async def execute(self, user: dto.User):
        email = user.email
        username = user.username
        password = user.password

        hashed_password = self._hasher.hash(password)
        user = entities.User(
            email=vo.Email(email),
            username=vo.UserName(username),
            hashed_password=vo.HashedPassword(hashed_password)
        )
        
        # try:
        await self._dao.create(user)
        # except IntegrityError:
        #     raise UserAlreadyExistsException
        await self._dao.commit()

