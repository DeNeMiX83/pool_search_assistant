from typing import Callable, Type
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, FastAPI
import pandas as pd

from app.infrastructure.store_data.db.sqlalchemy.connect import session_factory

from app.infrastructure.shared.dao import DAOProtocol
from app.infrastructure.store_data.db.dao.pool import PoolReadDAOImp, PoolWriteDAOImp
from app.core.pool.usecase.get_recommended_pools import GetRecommendedPoolsUseCase
from app.core.pool.protocols.pool_analysis import PoolAnalysisProtocol
from app.core.pool.services.pool_analysis import PoolAnalysisImp


def provide_usecase_stub():
    raise NotImplementedError

def provide_session_stub():
    raise NotImplementedError

def get_analyzer_stub() -> PoolAnalysisProtocol:
    raise NotImplementedError

def get_dao(
    dao_type: Type[DAOProtocol],
) -> Callable[[AsyncSession], DAOProtocol]:

    def _get_dao(
        session: AsyncSession = Depends(provide_session_stub),
    ) -> DAOProtocol:
        return dao_type(session)

    return _get_dao

def get_analyzer() -> PoolAnalysisProtocol:
    metadata = pd.read_csv('data.csv', low_memory=False)
    return PoolAnalysisImp(metadata)

def provide_get_recommended_pool(
    dao: DAOProtocol = Depends(get_dao(PoolReadDAOImp)),
    analyzer: PoolAnalysisProtocol = Depends(get_analyzer_stub),
) -> GetRecommendedPoolsUseCase:
    return GetRecommendedPoolsUseCase(analyzer, dao)


def setup_di(app: FastAPI):
    app.dependency_overrides[provide_session_stub] = session_factory
    app.dependency_overrides[provide_get_recommended_pool] = provide_get_recommended_pool
    app.dependency_overrides[get_analyzer_stub] = get_analyzer