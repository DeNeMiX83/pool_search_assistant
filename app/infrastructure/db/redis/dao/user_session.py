from app.core.user.protocols.dao.session_write import UserSessionWriteDao
from app.core.user import dto


class UserSessionWtiteDaoImp(UserSessionWriteDao):

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
    