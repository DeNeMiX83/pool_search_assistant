from redis.asyncio import Redis


def redis_factory(host: str, port: int, db: str) -> Redis:
    return Redis(
        host=host,
        port=port,
        db=db,
    )
