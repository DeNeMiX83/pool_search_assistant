from app.core.user import entities
from app.core.user.entities import value_objects as vo

from app.core.user.protocols.dao.user_write import UserWriteDao
from app.core.user.protocols.dao.user_read import UserReadDao
from app.infrastructure.db.sqlalchemy.dao.base import BaseDao

from sqlalchemy import select


class UserWriteDaoImp(BaseDao, UserWriteDao):
    async def create(self, user: entities.User) -> None:
        self._session.add(user)


class UserReadDaoImp(BaseDao, UserReadDao):
    async def get_by_email(self, email: vo.Email) -> entities.User:
        stmt = select(entities.User).where(entities.User.email == email)
        result = await self._session.execute(stmt)
        return result.scalars().first()

    async def get_by_username(self, username: vo.UserName) -> entities.User:
        stmt = select(entities.User).where(entities.User.username == username)
        result = await self._session.execute(stmt)
        return result.scalars().first()
