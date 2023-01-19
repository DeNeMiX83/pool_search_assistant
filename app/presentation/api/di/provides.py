from typing import Callable, Type
import pandas as pd
from sqlalchemy.ext.asyncio import AsyncSession
from redis.asyncio import Redis
from fastapi import Depends

from app.infrastructure.db.sqlalchemy import dao as sqlalchemy_dao
from app.infrastructure.db.redis import dao as redis_dao

#Pool
from app.core.pool import usecases as pool_usecases

from app.core.pool.protocols.pool_analysis import PoolAnalysis

from app.core.pool.services.pool_analysis import PoolAnalysisImp

#User
from app.core.user import usecases as user_usecases

from app.core.user.protocols.auth_sevice import AuthService
from app.core.user.protocols.hasher_password import HasherPassword
from app.core.user.protocols.jwt_service import JwtService

from app.core.user.services.auth_service import AuthServiceImp
from app.core.user.services.hasher_password import HasherPasswordImp
from app.core.user.services.jwt_service import JwtServiceImp


from app.presentation.api.di.stubs import (
    provide_session_stub,
    provide_redis_stub,
    get_analyzer_stub,
    get_auth_service_stub,
    get_hasher_password_stub,
    get_jwt_service_stub,
)

def get_sqlalchemy_dao(
    dao_type: Type[sqlalchemy_dao.Dao],
) -> Callable[[AsyncSession], sqlalchemy_dao.Dao]:

    def _get_dao(
        session: AsyncSession = Depends(provide_session_stub),
    ) -> sqlalchemy_dao.Dao:
        return dao_type(session)

    return _get_dao


def get_redis_dao(
    dao_type: Type[redis_dao.Dao],
) -> Callable[[Redis], redis_dao.Dao]:

    def _get_dao(
        session: Redis = Depends(provide_redis_stub),
    ) -> redis_dao.Dao:
        return dao_type(session)

    return _get_dao

#Pool
def provide_get_recommended_pool(
    dao: sqlalchemy_dao.Dao = Depends(get_sqlalchemy_dao(sqlalchemy_dao.PoolReadDaoImp)),
    analyzer: PoolAnalysis = Depends(get_analyzer_stub),
) -> pool_usecases.GetRecommendedPoolsUseCase:
    return pool_usecases.GetRecommendedPoolsUseCase(analyzer, dao)

def get_analyzer() -> PoolAnalysis:
    metadata = pd.read_csv('app/resources/data.csv', low_memory=False)
    return PoolAnalysisImp(metadata)

#User
def provide_register_user(
    auth_service: AuthService = Depends(get_auth_service_stub),
) -> user_usecases.RegisterUserUseCase:
    return user_usecases.RegisterUserUseCase(auth_service)

def provide_login_user(
    auth_service: AuthService = Depends(get_auth_service_stub),
) -> user_usecases.LoginUserUseCase:
    return user_usecases.LoginUserUseCase(auth_service)

def get_auth_service(
    hasher_password: HasherPassword = Depends(get_hasher_password_stub),
    jwt_service: JwtService = Depends(get_jwt_service_stub),
    user_session_dao: redis_dao.Dao = Depends(get_redis_dao(redis_dao.UserSessionWtiteDaoImp)),
    user_write_dao: sqlalchemy_dao.Dao = Depends(get_sqlalchemy_dao(sqlalchemy_dao.UserWriteDaoImp)),
    user_read_dao: sqlalchemy_dao.Dao = Depends(get_sqlalchemy_dao(sqlalchemy_dao.UserReadDaoImp)),
) -> AuthService:
    return AuthServiceImp(
        hasher_password,
        jwt_service,
        user_session_dao,
        user_write_dao,
        user_read_dao,
    )

def get_hasher_password() -> HasherPasswordImp:
    return HasherPasswordImp()

def get_jwt_service() -> JwtServiceImp:
    return JwtServiceImp()