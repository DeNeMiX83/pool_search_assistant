from app.shared.dto import WriteDto
from app.core.shared.entities.value_objects import UUID


class SessionWrite(WriteDto):
    session_id: UUID
    jwt_token: str
