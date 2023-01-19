from app.core.user import entities
from app.infrastructure.db.sqlalchemy.dao.base import WriteDao


class UserWriteDao(WriteDao):
    
    async def create(self, user: entities.User) -> None:
        raise NotImplementedError