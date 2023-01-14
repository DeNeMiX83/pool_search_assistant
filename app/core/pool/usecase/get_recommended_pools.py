from app.core.shared.usecase.usecase import UseCase
from app.core.shared.entities.value_objects.uuid import UUID
from app.core.pool.entities.pool import PoolEntity
from app.core.pool.protocols.pool_analysis import PoolAnalysisProtocol
from app.core.pool.protocols.dao.pool_read_dao import PoolReadDAOProtocol



class GetRecommendedPoolsUseCase(UseCase):
    def __init__(self, analyzer: PoolAnalysisProtocol, dao: PoolReadDAOProtocol):
        self._analyzer = analyzer
        self._dao = dao

    async def execute(self, selected_pool_id: UUID) -> list[PoolEntity]:
        pool = await self._dao.get_pool_by_id(selected_pool_id)
        recomended_pools = self._analyzer.get_recommended_pools(pool)
        return recomended_pools

