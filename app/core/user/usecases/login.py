from app.core.shared.usecase.usecase import UseCase
from app.core.user.protocols.dao.user_read import UserReadDao
from app.core.user import dto

from app.core.user.services.auth_service import AuthService



class LoginUserUseCase(UseCase):

    def __init__(
        self, 
        auth_service: AuthService,
    ):
        self._auth_service = auth_service
    async def execute(self, user: dto.UserLogin) -> str:
        return await self._auth_service.login(user)

        

        

        

        