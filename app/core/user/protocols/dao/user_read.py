from app.core.shared.entities.value_objects.email import Email
from app.core.user.entities.value_objects.username import UserName
from app.infrastructure.store_data.dao.base import ReadDao


class UserReadDao(ReadDao):
    
    async def get_by_email(self, email: Email):
        raise NotImplementedError

    async def get_by_username(self, username: UserName):
        raise NotImplementedError