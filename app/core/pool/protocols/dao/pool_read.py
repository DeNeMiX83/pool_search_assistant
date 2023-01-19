from app.infrastructure.store_data.dao.base import ReadDao
from app.core.pool import entities


class PoolReadDao(ReadDao):
    
    async def get_by_id(self, pool_id: int) -> entities.Pool:
        raise NotImplementedError