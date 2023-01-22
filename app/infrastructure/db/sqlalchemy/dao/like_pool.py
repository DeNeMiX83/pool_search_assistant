from sqlalchemy import select, and_
from app.core.shared.entities import value_objects as vo
from app.core.pool import entities
from app.core.pool.protocols.dao.like_pool_write import LikePoolWriteDao
from app.core.pool.protocols.dao.like_pool_read import LikePoolReadDao
from app.infrastructure.db.sqlalchemy.dao.base import BaseDao


class LikePoolWriteDaoImp(
    BaseDao, LikePoolWriteDao
):
    async def create(self, like_pool: entities.PoolLike) -> None:
        await self._session.add(like_pool)

    async def delete(self, like_pool: entities.PoolLike) -> None:
        await self._session.delete(like_pool)


class LikePoolReadDaoImp(
    BaseDao, LikePoolReadDao
):
    async def get_by_pool_id_user_id(
        self, pool_id: int, user_id: vo.UUID
    ) -> entities.PoolLike:
        stmt = select(entities.PoolLike).where(and_(
            entities.PoolLike.pool_id == pool_id,
            entities.PoolLike.user_id == user_id
        ))
        result = await self._session.execute(stmt)
        return result.scalars().first()
