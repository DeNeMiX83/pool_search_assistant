from app.shared.dto import WriteDto


class User(WriteDto):
    email: str
    password: str


class UserLogin(User):
    pass