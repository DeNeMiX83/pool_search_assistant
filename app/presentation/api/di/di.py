from fastapi import FastAPI

from app.infrastructure.store_data.db.sqlalchemy.connect import session_factory

from app.presentation.api.di.stubs import (
    provide_session_stub,
    provide_get_recommended_pool_stub,
    get_analyzer_stub,
    provide_register_user_stub,
    get_hasher_stub
)

from app.presentation.api.di.provides import (
    provide_get_recommended_pool,
    get_analyzer,
    provide_register_user,
    get_hasher
)


def setup_di(app: FastAPI):
    app.dependency_overrides[provide_session_stub] = session_factory
    app.dependency_overrides[provide_get_recommended_pool_stub] = provide_get_recommended_pool
    app.dependency_overrides[get_analyzer_stub] = get_analyzer
    app.dependency_overrides[provide_register_user_stub] = provide_register_user
    app.dependency_overrides[get_hasher_stub] = get_hasher

    # app.dependency_overrides.update({
    #     provide_session_stub: session_factory,
    # })