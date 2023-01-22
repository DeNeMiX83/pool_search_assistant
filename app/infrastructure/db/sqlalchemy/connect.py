from sqlalchemy.ext.asyncio import (
    AsyncSession, create_async_engine
)
from sqlalchemy.orm import sessionmaker


def create_session_factory(url: str) -> AsyncSession:

    engine = create_async_engine(url, echo=True)

    async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )

    async def session_factory() -> AsyncSession:
        async with async_session() as session:
            yield session

    return session_factory
