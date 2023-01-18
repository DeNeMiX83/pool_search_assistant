from app.core.user import entities
from app.infrastructure.store_data.dao.base import WriteDao


class UserWrite(WriteDao):
    
    async def create(self, user: entities.User) -> None:
        raise NotImplementedError