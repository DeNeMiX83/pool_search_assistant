from app.infrastructure.store_data.dao.base import ReadDao
from app.core.pool.entities.pool import Pool
from app.core.shared.entities.value_objects.uuid import UUID


class PoolReadDao(ReadDao):
    
    async def get_pool_by_id(self, pool_id: UUID) -> Pool:
        raise NotImplementedError