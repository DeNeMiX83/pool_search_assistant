from typing import Protocol
from app.core.shared.entities import value_objects as vo
from app.core.pool import entities


class LikePoolReadDao(Protocol):
    async def get_by_pool_id_user_id(
        self, pool_id: int, user_id: vo.UUID
    ) -> entities.PoolLike:
        raise NotImplementedError
