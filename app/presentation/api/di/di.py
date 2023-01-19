from fastapi import FastAPI

from app.infrastructure.db.sqlalchemy.connect import session_factory
from app.infrastructure.db.redis.connect import redis_factory

from app.presentation.api.di.stubs import (
    provide_session_stub,
    provide_redis_stub,

    provide_get_recommended_pool_stub,
    get_analyzer_stub,

    provide_register_user_stub,
    provide_login_user_stub,
    get_auth_service_stub,
    get_hasher_password_stub,
    get_jwt_service_stub,
)

from app.presentation.api.di.provides import (
    provide_get_recommended_pool,
    get_analyzer,
    provide_register_user,
    provide_login_user,
    get_auth_service,
    get_hasher_password,
    get_jwt_service,
)


def setup_di(app: FastAPI):
    app.dependency_overrides[provide_session_stub] = session_factory
    app.dependency_overrides[provide_redis_stub] = redis_factory

    app.dependency_overrides[provide_get_recommended_pool_stub] = provide_get_recommended_pool
    app.dependency_overrides[get_analyzer_stub] = get_analyzer

    app.dependency_overrides[provide_register_user_stub] = provide_register_user
    app.dependency_overrides[provide_login_user_stub] = provide_login_user
    app.dependency_overrides[get_auth_service_stub] = get_auth_service
    app.dependency_overrides[get_hasher_password_stub] = get_hasher_password
    app.dependency_overrides[get_jwt_service_stub] = get_jwt_service

    # app.dependency_overrides.update({
    #     provide_session_stub: session_factory,
    # })