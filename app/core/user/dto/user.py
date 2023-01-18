from app.shared.dto import WriteDto


class User(WriteDto):
    email: str
    username: str
    password: str