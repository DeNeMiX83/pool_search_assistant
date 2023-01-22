from sqlalchemy.exc import IntegrityError
from app.core.shared.usecase import UseCase
from app.core.pool import entities
from app.core.pool import dto
from app.core.pool.protocols.dao import LikePoolWriteDao
from app.core.shared.protocols import Committer


class LikePoolUseCase(UseCase[dto.PoolLike, None]):
    def __init__(
        self,
        dao: LikePoolWriteDao,
        committer: Committer,
    ):
        self._dao = dao
        self._committer = committer

    async def execute(self, pool_like_dto: dto.PoolLike) -> None:
        pool_like = entities.PoolLike(
            pool_id=pool_like_dto.pool_id,
            user_id=pool_like_dto.user_id,
        )

        await self._dao.create(pool_like)

        try:
            await self._committer.commit()
        except IntegrityError:
            await self._committer.rollback()
            raise ValueError("Pool not found or user already liked it")
