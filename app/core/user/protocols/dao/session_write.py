from app.infrastructure.db.redis.dao.base import WriteDao
from app.core.user import dto


class UserSessionWriteDao(WriteDao):

    async def create(self, session: dto.SessionWrite) -> None:
        raise NotImplementedError

    async def update(self, session: dto.SessionWrite) -> None:
        raise NotImplementedError

    async def delete(self, session: dto.SessionWrite) -> None:
        raise NotImplementedError
    