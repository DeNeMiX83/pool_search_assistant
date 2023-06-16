from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from app.presentation.api.di.di import setup_di

from app.presentation.api.routes import router

from app.infrastructure.db.sqlalchemy.models.mapping import start_mappers
from app.settings import Settings
from .open_api import set_custom_openapi


def create_app() -> FastAPI:
    settings = Settings()

    app = FastAPI(
        root_path=settings.root_path,
        docs_url=settings.docs_url,
    )
    start_mappers()
    setup_di(app, settings)

    app.include_router(router)
    set_custom_openapi(app, settings)

    return app


app = create_app()
