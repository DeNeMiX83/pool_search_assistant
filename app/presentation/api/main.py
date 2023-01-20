from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from app.presentation.api.di.di import setup_di

from app.presentation.api.routes import router

from app.infrastructure.db.sqlalchemy.models.mapping import start_mappers


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Pool search API",
        version="1.0.0",
        description="The data is taken from the open data source at the link: \n\
                     https://data.mos.ru/opendata/7708308010-basseyny-plavatelnye-krytye",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema



def create_app() -> FastAPI:
    app = FastAPI()

    start_mappers()
    setup_di(app)
    app.include_router(router)
    
    return app


app = create_app()
app.openapi = custom_openapi

