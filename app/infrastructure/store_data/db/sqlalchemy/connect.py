from sqlalchemy.ext.asyncio import (
    AsyncSession, create_async_engine
)
from sqlalchemy.orm import sessionmaker

from app.settings import PostgresSettings

postgres_settings = PostgresSettings()
DATABASE_URL = postgres_settings.dsn()


engine = create_async_engine(DATABASE_URL, echo=True)



async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

async def session_factory() -> AsyncSession:
    async with async_session() as session:
        yield session

# async def init_models():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.drop_all)
#         await conn.run_sync(Base.metadata.create_all)