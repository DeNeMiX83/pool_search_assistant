from app.core.shared.entities.value_objects.email import Email
from app.core.user.entities.value_objects.username import UserName
from app.core.user import entities

from app.infrastructure.db.sqlalchemy.dao.base import ReadDao

class UserReadDao(ReadDao):
    
    async def get_by_email(self, email: Email) -> entities.User:
        raise NotImplementedError

    async def get_by_username(self, username: UserName) -> entities.User:
        raise NotImplementedError