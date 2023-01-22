from typing import Protocol
from app.core.pool import entities


class LikePoolWriteDao(Protocol):
    async def create(self, pool_like: entities.PoolLike) -> None:
        raise NotImplementedError

    async def delete(self, pool_like: entities.PoolLike) -> None:
        raise NotImplementedError
