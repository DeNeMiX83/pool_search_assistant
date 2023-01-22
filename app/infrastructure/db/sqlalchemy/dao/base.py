from typing import Protocol
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.shared.protocols.commiter import Committer


class Dao(Protocol):
    def __init__(self, session: AsyncSession) -> None:
        raise NotImplementedError


class BaseDao(Dao):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session


class CommitterImp(BaseDao, Committer):
    async def commit(self) -> None:
        await self._session.commit()

    async def rollback(self) -> None:
        await self._session.rollback()
