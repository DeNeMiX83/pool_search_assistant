from typing import Protocol
from app.core.user import dto


class UserSessionWriteDao(Protocol):

    async def create(self, session: dto.SessionWrite) -> None:
        raise NotImplementedError

    async def update(self, session: dto.SessionWrite) -> None:
        raise NotImplementedError

    async def delete(self, session: dto.SessionWrite) -> None:
        raise NotImplementedError
