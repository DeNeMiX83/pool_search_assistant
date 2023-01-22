from app.core.user.services import AuthService
from app.core.user import dto


class LogoutUserUseCase:

    def __init__(
        self,
        auth_service: AuthService,
    ):
        self._auth_service = auth_service

    async def execute(self, user: dto.UserLogout) -> None:
        await self._auth_service.logout(user)
