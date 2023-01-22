from app.shared.dto import BaseDto
from app.core.shared.entities.value_objects import UUID


class SessionRead(BaseDto):
    jwt_token: str | None


class SessionWrite(SessionRead):
    session_id: UUID
    jwt_token: str
