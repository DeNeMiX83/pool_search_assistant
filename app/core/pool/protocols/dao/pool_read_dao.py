from app.infrastructure.shared.dao import ReadDAOProtocol
from app.core.pool.entities.pool import PoolEntity
from app.core.shared.entities.value_objects.uuid import UUID


class PoolReadDAOProtocol(ReadDAOProtocol):
    
    def get_pool_by_id(self, pool_id: UUID) -> PoolEntity:
        raise NotImplementedError