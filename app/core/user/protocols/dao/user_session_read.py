from typing import Protocol
from app.core.user import dto


class UserSessionReadDao(Protocol):
    async def get(self, session_id: str) -> dto.SessionRead:
        raise NotImplementedError
