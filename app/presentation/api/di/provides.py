from typing import Callable, Type
import pandas as pd
from sqlalchemy.ext.asyncio import AsyncSession
from redis.asyncio import Redis
from fastapi import Depends, Header, HTTPException, status

from app.infrastructure.db.sqlalchemy import dao as sqlalchemy_dao
from app.infrastructure.db.redis import dao as redis_dao

# Pool
from app.core.pool import usecases as pool_usecases
from app.core.pool import dto as pool_dto

from app.core.pool.protocols.pool_analysis import PoolAnalysis

from app.core.pool.services.pool_analysis import PoolAnalysisImp

# User
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
    provide_analyzer_stub,
    provide_auth_service_stub,
    provide_hasher_password_stub,
    provide_jwt_service_stub,
    get_user_data_by_session_id_stub,
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
        redis: Redis = Depends(provide_redis_stub),
    ) -> redis_dao.Dao:
        return dao_type(redis)

    return _get_dao


# Pool
def provide_get_recommended_pool(
    dao: sqlalchemy_dao.Dao = Depends(
        get_sqlalchemy_dao(sqlalchemy_dao.PoolReadDaoImp)
    ),
    analyzer: PoolAnalysis = Depends(provide_analyzer_stub),
) -> pool_usecases.GetRecommendedPoolsUseCase:
    return pool_usecases.GetRecommendedPoolsUseCase(analyzer, dao)


def provide_analyzer() -> PoolAnalysis:
    metadata = pd.read_csv("app/resources/data.csv", low_memory=False)
    return PoolAnalysisImp(metadata)


def provide_like_pool(
    dao: sqlalchemy_dao.Dao = Depends(
        get_sqlalchemy_dao(sqlalchemy_dao.LikePoolWriteDaoImp)
    ),
    committer: sqlalchemy_dao.Dao = Depends(
        get_sqlalchemy_dao(sqlalchemy_dao.CommitterImp)
    ),
) -> pool_usecases.LikePoolUseCase:
    return pool_usecases.LikePoolUseCase(dao, committer)


def provide_unlike_pool(
    dao_read: sqlalchemy_dao.Dao = Depends(
        get_sqlalchemy_dao(sqlalchemy_dao.LikePoolReadDaoImp)
    ),
    dao_write: sqlalchemy_dao.Dao = Depends(
        get_sqlalchemy_dao(sqlalchemy_dao.LikePoolWriteDaoImp)
    ),
    committer: sqlalchemy_dao.Dao = Depends(
        get_sqlalchemy_dao(sqlalchemy_dao.CommitterImp)
    ),
) -> pool_usecases.UnlikePoolUseCase:
    return pool_usecases.UnlikePoolUseCase(dao_read, dao_write, committer)


async def get_like_pools_by_user_id(
    user_data: dict = Depends(get_user_data_by_session_id_stub),
    dao: sqlalchemy_dao.Dao = Depends(
        get_sqlalchemy_dao(sqlalchemy_dao.LikePoolReadDaoImp)
    ),
) -> list[pool_dto.PoolLike]:
    return await dao.get_by_user_id(user_data["user_id"])


# User
def provide_register_user(
    auth_service: AuthService = Depends(provide_auth_service_stub),
) -> user_usecases.RegisterUserUseCase:
    return user_usecases.RegisterUserUseCase(auth_service)


def provide_login_user(
    auth_service: AuthService = Depends(provide_auth_service_stub),
) -> user_usecases.LoginUserUseCase:
    return user_usecases.LoginUserUseCase(auth_service)


def provide_logout_user(
    auth_service: AuthService = Depends(provide_auth_service_stub),
) -> user_usecases.LogoutUserUseCase:
    return user_usecases.LogoutUserUseCase(auth_service)


def provide_auth_service(
    hasher_password: HasherPassword = Depends(provide_hasher_password_stub),
    jwt_service: JwtService = Depends(provide_jwt_service_stub),
    user_session_dao_read: redis_dao.Dao = Depends(
        get_redis_dao(redis_dao.UserSessionReadDaoImp)
    ),
    user_session_dao_write: redis_dao.Dao = Depends(
        get_redis_dao(redis_dao.UserSessionWtiteDaoImp)
    ),
    user_write_dao: sqlalchemy_dao.Dao = Depends(
        get_sqlalchemy_dao(sqlalchemy_dao.UserWriteDaoImp)
    ),
    user_read_dao: sqlalchemy_dao.Dao = Depends(
        get_sqlalchemy_dao(sqlalchemy_dao.UserReadDaoImp)
    ),
    committer: sqlalchemy_dao.Dao = Depends(
        get_sqlalchemy_dao(sqlalchemy_dao.CommitterImp)
    ),
) -> AuthService:
    return AuthServiceImp(
        hasher_password=hasher_password,
        jwt_service=jwt_service,
        dao_user_session_write=user_session_dao_write,
        dao_user_session_read=user_session_dao_read,
        dao_user_write=user_write_dao,
        dao_user_read=user_read_dao,
        committer=committer,
    )


def provide_hasher_password() -> HasherPasswordImp:
    return HasherPasswordImp()


def provide_jwt_service() -> JwtServiceImp:
    return JwtServiceImp()


async def get_user_data_by_session_id(
    session_id: str = Header(...),
    dao: redis_dao.Dao = Depends(
        get_redis_dao(redis_dao.UserSessionReadDaoImp)
    ),
    jwt_service: JwtService = Depends(provide_jwt_service_stub),
):
    try:
        session_data = await dao.get(session_id)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e))

    user_data = jwt_service.decode(session_data.jwt_token)
    return user_data
