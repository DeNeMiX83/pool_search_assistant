from typing import Protocol
from app.core.user import entities


class AuthService(Protocol):

    async def login(self, user: entities.User) -> str:
        raise NotImplementedError

    async def register(self, user: entities.User) -> str:
        raise NotImplementedError


