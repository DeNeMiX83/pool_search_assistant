from typing import Protocol
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.shared.entities.entity import Entity
from app.core.shared.entities.value_objects.uuid import UUID


class Dao(Protocol):

    def __init__(self, session) -> None:
        raise NotImplementedError
    
    def commit(self) -> None:
        raise NotImplementedError


class BaseDao(Dao):

    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def commit(self) -> None:
        await self._session.commit()


class ReadDao(BaseDao):

    async def get(self, id: UUID) -> dict:
        raise NotImplementedError

    async def get_all(self) -> list:
        raise NotImplementedError


class WriteDao(BaseDao):
    
    async def create(self, obj: Entity) -> None:
        raise NotImplementedError

    async def update(self, obj: Entity) -> None:
        raise NotImplementedError

    async def delete(self, obj: Entity) -> None:
        raise NotImplementedError
    