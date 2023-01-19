from app.core.shared.usecase.usecase import UseCase
from app.core.shared.entities.value_objects.uuid import UUID
from app.core.pool import entities
from app.core.pool.protocols.pool_analysis import PoolAnalysis
from app.core.pool.protocols.dao.pool_read import PoolReadDao



class GetRecommendedPoolsUseCase(UseCase):
    def __init__(self, analyzer: PoolAnalysis, dao: PoolReadDao):
        self._analyzer = analyzer
        self._dao = dao

    async def execute(self, selected_pool_id: UUID) -> list[entities.Pool]:
        pool = await self._dao.get_by_id(selected_pool_id)
        recomended_pools_id = self._analyzer.get_recommended_pools_id(pool)
        recomended_pools = []
        for id in recomended_pools_id:
            pool = await self._dao.get_by_id(id)
            recomended_pools.append(pool)
        return recomended_pools

