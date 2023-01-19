from passlib.context import CryptContext
from app.core.user.protocols.hasher_password import HasherPassword


class HasherPasswordImp(HasherPassword):
    _pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def hash(self, password: str) -> str:
        return self._pwd_context.hash(password)

    def verify_password(self, raw_password: str, hashed_password: str) -> bool:
        return self._pwd_context.verify(raw_password, hashed_password)