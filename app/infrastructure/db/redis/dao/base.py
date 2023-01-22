from typing import Protocol
from redis.asyncio import Redis


class Dao(Protocol):

    def __init__(self, redis) -> None:
        raise NotImplementedError


class BaseDao(Dao):

    def __init__(self, redis: Redis) -> None:
        self._redis = redis
