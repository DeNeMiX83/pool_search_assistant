from typing import Protocol
from app.core.user import entities
from app.core.user import dto


class AuthService(Protocol):

    async def login(self, user: entities.User) -> str:
        raise NotImplementedError

    async def register(self, user: dto.UserRegister) -> None:
        raise NotImplementedError

    async def logout(self, user: dto.UserLogout) -> None:
        raise NotImplementedError


