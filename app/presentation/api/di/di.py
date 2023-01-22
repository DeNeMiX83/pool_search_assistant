from fastapi import FastAPI

from app.infrastructure.db.sqlalchemy.connect import create_session_factory
from app.infrastructure.db.redis.connect import redis_factory

from app.settings import Settings

from app.presentation.api.di import (
    provide_session_stub,
    provide_redis_stub,
    provide_get_recommended_pool_stub,
    provide_analyzer_stub,
    provide_like_pool_stub,
    provide_unlike_pool_stub,
    provide_register_user_stub,
    provide_login_user_stub,
    provide_logout_user_stub,
    provide_auth_service_stub,
    provide_hasher_password_stub,
    provide_jwt_service_stub,
    get_user_data_by_session_id_stub,
)

from app.presentation.api.di.provides import (
    provide_get_recommended_pool,
    provide_analyzer,
    provide_like_pool,
    provide_unlike_pool,
    provide_register_user,
    provide_login_user,
    provide_logout_user,
    provide_auth_service,
    provide_hasher_password,
    provide_jwt_service,
    get_user_data_by_session_id,
)


def setup_di(app: FastAPI, settings: Settings):
    session_factory = create_session_factory(settings.postgres_url)
    redis = redis_factory(
        host=settings.redis.host,
        port=settings.redis.port,
        db=settings.redis.db,
    )

    app.dependency_overrides.update({
        provide_session_stub: session_factory,
        provide_redis_stub: lambda: redis,
    })

    app.dependency_overrides.update({
        provide_get_recommended_pool_stub: provide_get_recommended_pool,
        provide_analyzer_stub: provide_analyzer,
        provide_like_pool_stub: provide_like_pool,
        provide_unlike_pool_stub: provide_unlike_pool,
    })

    app.dependency_overrides.update({
        provide_register_user_stub: provide_register_user,
        provide_login_user_stub: provide_login_user,
        provide_logout_user_stub: provide_logout_user,
        provide_auth_service_stub: provide_auth_service,
        provide_hasher_password_stub: provide_hasher_password,
        provide_jwt_service_stub: provide_jwt_service,
        get_user_data_by_session_id_stub: get_user_data_by_session_id,
    })
