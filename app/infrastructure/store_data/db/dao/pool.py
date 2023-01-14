from sqlalchemy import select

from app.core.pool.protocols.dao.pool_read_dao import PoolReadDAOProtocol
from app.core.pool.protocols.dao.pool_write_dao import PoolWriteDAOProtocol
from app.core.pool.entities.pool import PoolEntity
from app.core.shared.entities.value_objects.uuid import UUID


class PoolReadDAOImp(PoolReadDAOProtocol):
    
    async def get_pool_by_id(self, pool_id: UUID) -> PoolEntity:
        stmt = select(PoolEntity).where(PoolEntity.id == pool_id)
        result = await self._session.execute(stmt)
        return result.scalars().first()

class PoolWriteDAOImp(PoolWriteDAOProtocol):
    ...