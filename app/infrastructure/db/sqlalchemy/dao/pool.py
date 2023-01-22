from sqlalchemy import select

from app.core.pool import entities

from app.infrastructure.db.sqlalchemy.dao.base import BaseDao
from app.core.pool.protocols.dao.pool_read import PoolReadDao


class PoolReadDaoImp(BaseDao, PoolReadDao):
    async def get(self, pool_id: int) -> entities.Pool:
        stmt = select(entities.Pool).where(entities.Pool.id == pool_id)
        result = await self._session.execute(stmt)
        return result.scalars().first()