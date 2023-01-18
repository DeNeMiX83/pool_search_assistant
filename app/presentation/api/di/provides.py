from typing import Callable, Type
import pandas as pd
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends

from app.infrastructure.store_data import dao

#Pool
from app.core.pool import usecases as pool_usecases
from app.core.pool.protocols.pool_analysis import PoolAnalysis
from app.core.pool.services.pool_analysis import PoolAnalysisImp

#User
from app.core.user import usecases as user_usecases
from app.core.user.protocols.hasher_password import HasherPassword
from app.core.user.services.hasher_password import HasherPasswordImp

from app.presentation.api.di.stubs import (
    provide_session_stub,
    get_analyzer_stub,
    get_hasher_stub,
)

def get_dao(
    dao_type: Type[dao.Dao],
) -> Callable[[AsyncSession], dao.Dao]:

    def _get_dao(
        session: AsyncSession = Depends(provide_session_stub),
    ) -> dao.Dao:
        return dao_type(session)

    return _get_dao

#Pool
def provide_get_recommended_pool(
    dao: dao.Dao = Depends(get_dao(dao.PoolReadDaoImp)),
    analyzer: PoolAnalysis = Depends(get_analyzer_stub),
) -> pool_usecases.GetRecommendedPoolsUseCase:
    return pool_usecases.GetRecommendedPoolsUseCase(analyzer, dao)

def get_analyzer() -> PoolAnalysis:
    metadata = pd.read_csv('data.csv', low_memory=False)
    return PoolAnalysisImp(metadata)

#User
def provide_register_user(
    dao: dao.Dao = Depends(get_dao(dao.UserWriteImp)),
    hasher: HasherPassword = Depends(get_hasher_stub),
) -> user_usecases.RegisterUserUseCase:
    return user_usecases.RegisterUserUseCase(dao, hasher)

def get_hasher() -> HasherPassword:
    return HasherPasswordImp()