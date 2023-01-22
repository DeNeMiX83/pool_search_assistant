from typing import Protocol
from app.core.user import entities


class UserWriteDao(Protocol):
    async def create(self, user: entities.User) -> None:
        raise NotImplementedError
