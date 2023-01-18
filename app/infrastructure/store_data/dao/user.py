from sqlalchemy import insert
from dataclasses import asdict

from app.core.user import entities

from app.core.user.protocols.dao.user_write import UserWrite
from app.core.user.protocols.dao.user_read import UserReadDao




class UserWriteImp(UserWrite):
    
    async def create(self, user: entities.User) -> None:
        self._session.add(user)
    

class UserReadImp(UserReadDao):
    
    ...
