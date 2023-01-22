from app.infrastructure.db.redis.dao.base import BaseDao
from app.core.user.protocols.dao.user_session_write import UserSessionWriteDao
from app.core.user.protocols.dao.user_session_read import UserSessionReadDao
from app.core.user import dto


class UserSessionWtiteDaoImp(BaseDao, UserSessionWriteDao):

    async def create(self, session: dto.SessionWrite) -> None:
        session_id = str(session.session_id)
        jwt_token = session.jwt_token

        await self._redis.set(session_id, jwt_token)

    async def update(self, session: dto.SessionWrite) -> None:
        session_id = session.session_id
        jwt_token = session.jwt_token

        await self._redis.set(session_id, jwt_token)

    async def delete(self, session: dto.SessionWrite) -> None:
        session_id = session.session_id
        await self._redis.delete(session_id)


class UserSessionReadDaoImp(BaseDao, UserSessionReadDao):

    async def get(self, session_id: str) -> dto.SessionRead | None:
        if not session_id:
            return None
        jwt_token = await self._redis.get(session_id)
        if not jwt_token:
            return None
        return dto.SessionRead(jwt_token=jwt_token)
