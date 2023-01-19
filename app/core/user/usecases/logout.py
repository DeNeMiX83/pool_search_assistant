from app.core.user.services import AuthService


class LogoutUserUseCase:

    def __init__(
        self,
        auth_service: AuthService,
    ):
        self._auth_service = auth_service

    def execute(self, session_id: str) -> None:
        return self._auth_service.logout(session_id)