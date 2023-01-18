from sqlalchemy import select

from app.core.pool import entities

from app.core.pool.protocols.dao.pool_read import PoolReadDao
from app.core.shared.entities.value_objects.uuid import UUID


class PoolReadDaoImp(PoolReadDao):
    
    async def get_pool_by_id(self, pool_id: UUID) -> entities.Pool:
        stmt = select(entities.Pool).where(entities.Pool.id == pool_id)
        result = await self._session.execute(stmt)
        return result.scalars().first()