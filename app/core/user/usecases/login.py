from app.core.user import entities
from app.core.user.entities import value_objects as vo

from app.core.shared.usecase.usecase import UseCase
from app.core.user.protocols.dao.user_read import UserReadDao
from app.core.user import dto
from app.core.user.exceptions.user import UserNotFoundError, InvalidPasswordError

from app.core.user.protocols.hasher_password import HasherPassword



class LoginUserUseCase(UseCase):

    def __init__(
        self, 
        dao: UserReadDao,
        hasher: HasherPassword
    ):
        self._dao = dao
        self._hasher = hasher

    def execute(self, user: dto.User) -> str:
        user = self._dao.get_by_email(user.email)

        if not user:
            raise UserNotFoundError()
        if not user.check_password(user.password):
            raise InvalidPasswordError()

        return 