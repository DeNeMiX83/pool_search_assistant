from fastapi import FastAPI
from app.presentation.api.di import setup_di

from app.presentation.api.routes import router

from app.infrastructure.store_data.db.sqlalchemy.models.mapping import start_mappers


def create_app() -> FastAPI:
    app = FastAPI()

    start_mappers()
    setup_di(app)
    app.include_router(router)
    
    return app


app = create_app()

