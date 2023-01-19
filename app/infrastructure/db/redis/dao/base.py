from typing import Protocol
from redis.asyncio import Redis
from app.shared import dto

class Dao(Protocol):

    def __init__(self, redis) -> None:
        raise NotImplementedError


class BaseDao(Dao):

    def __init__(self, redis: Redis) -> None:
        self._redis = redis


class ReadDao(BaseDao):

    async def get(self, key: str) -> dict:
        raise NotImplementedError


class WriteDao(BaseDao):
    
    async def create(self, obj: dto.WriteDto) -> None:
        raise NotImplementedError

    async def update(self, obj: dto.WriteDto) -> None:
        raise NotImplementedError

    async def delete(self, obj: dto.WriteDto) -> None:
        raise NotImplementedError
    