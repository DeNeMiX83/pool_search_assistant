from sqlalchemy.exc import InvalidRequestError
from app.core.shared.usecase import UseCase
from app.core.pool import dto
from app.core.pool.protocols.dao import LikePoolWriteDao
from app.core.pool.protocols.dao import LikePoolReadDao
from app.core.shared.protocols import Committer


class UnlikePoolUseCase(UseCase[dto.PoolLike, None]):
    def __init__(
        self,
        dao_read: LikePoolReadDao,
        dao_write: LikePoolWriteDao,
        committer: Committer,
    ):
        self._dao_read = dao_read
        self._dao_write = dao_write
        self._committer = committer

    async def execute(self, pool_unlike_dto: dto.PoolLike) -> None:
        user_id = pool_unlike_dto.user_id
        pool_id = pool_unlike_dto.pool_id

        pool_like = await self._dao_read.get_by_pool_id_user_id(
            pool_id=pool_id, user_id=user_id
        )

        try:
            await self._dao_write.delete(pool_like)
        except InvalidRequestError:
            await self._committer.rollback()
            raise ValueError("Pool not found")

        await self._committer.commit()
