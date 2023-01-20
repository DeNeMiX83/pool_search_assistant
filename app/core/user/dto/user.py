from app.shared.dto import WriteDto
from app.shared.dto import BaseDto


class User(WriteDto):
    email: str
    password: str


class UserLogin(User):
    pass


class UserLogout(BaseDto):
    session_id: str