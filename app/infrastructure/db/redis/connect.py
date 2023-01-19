from redis.asyncio import Redis
from app.settings import RedisSettings

settings = RedisSettings()

async def redis_factory() -> Redis:
    return Redis(
        host=settings.host,
        port=settings.port,
        db=settings.db,
    )

    