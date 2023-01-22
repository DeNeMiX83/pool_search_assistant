from typing import Protocol
from app.core.pool import entities


class PoolReadDao(Protocol):
    async def get(self, pool_id: int) -> entities.Pool:
        raise NotImplementedError
