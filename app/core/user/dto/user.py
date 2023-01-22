from app.shared.dto import BaseDto


class User(BaseDto):
    email: str


class UserLogin(User):
    email: str
    password: str


class UserRegister(User):
    username: str
    raw_password: str


class UserLogout(BaseDto):
    session_id: str
