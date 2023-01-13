from app.core.shared.usecase.usecase import UseCase
from app.core.shared.entities.value_objects.uuid import UUID
from app.core.pool.entities.pool import PoolEntity
from app.core.pool.protocols.pool_analysis import PoolAnalysisProtocol
from app.core.pool.protocols.dao.pool_read_dao import PoolReadDAOProtocol



class GetRecommendedPoolsUseCase(UseCase):
    def __init__(self, analyzer: PoolAnalysisProtocol, DAO: PoolReadDAOProtocol):
        self.analyzer = analyzer
        self.DAO = DAO

    def execute(self, selected_pool_id: UUID) -> list[PoolEntity]:
        recomended_pools = self.analyzer.get_recommended_pools(selected_pool_id)
        return recomended_pools

