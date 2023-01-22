from app.core.shared.usecase.usecase import UseCase
from app.core.pool import entities
from app.core.pool import dto
from app.core.pool.protocols.pool_analysis import PoolAnalysis
from app.core.pool.protocols.dao.pool_read import PoolReadDao


class GetRecommendedPoolsUseCase(UseCase[dto.LikePools, list[entities.Pool]]):
    def __init__(
        self,
        analyzer: PoolAnalysis,
        dao: PoolReadDao
    ):
        self._analyzer = analyzer
        self._dao = dao

    async def execute(self, like_pools: dto.LikePools) -> list[entities.Pool]:
        pool = await self._dao.get(like_pools.pool_ids[0])
        recomended_pools = self._analyzer.get_recommended_pools_id(pool)
        return recomended_pools
