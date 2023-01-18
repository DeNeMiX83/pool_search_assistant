from app.core.shared.usecase.usecase import UseCase
from app.core.shared.entities.value_objects.uuid import UUID
from app.core.pool.entities.pool import Pool
from app.core.pool.protocols.pool_analysis import PoolAnalysis
from app.core.pool.protocols.dao.pool_read import PoolReadDao



class GetRecommendedPoolsUseCase(UseCase):
    def __init__(self, analyzer: PoolAnalysis, dao: PoolReadDao):
        self._analyzer = analyzer
        self._dao = dao

    async def execute(self, selected_pool_id: UUID) -> list[Pool]:
        pool = await self._dao.get_pool_by_id(selected_pool_id)
        recomended_pools = self._analyzer.get_recommended_pools(pool)
        return recomended_pools

