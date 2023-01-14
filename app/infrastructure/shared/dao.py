from typing import Protocol
from sqlalchemy.ext.asyncio import AsyncSession



class DAOProtocol(Protocol):

    def __init__(self, session) -> None:
        raise NotImplementedError
    
    def commit(self) -> None:
        raise NotImplementedError


class BaseDAO(DAOProtocol):

    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def commit(self) -> None:
        await self._session.commit()


class ReadDAOProtocol(BaseDAO):

    def get(self, id: int) -> dict:
        raise NotImplementedError

    def get_all(self) -> list:
        raise NotImplementedError


class WriteDAOProtocol(BaseDAO):
    
    def create(self, data: dict) -> None:
        raise NotImplementedError

    def update(self, data: dict) -> None:
        raise NotImplementedError

    def delete(self, data: dict) -> None:
        raise NotImplementedError
    