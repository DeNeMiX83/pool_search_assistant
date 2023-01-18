from passlib.context import CryptContext
from app.core.user.protocols.hasher_password import HasherPassword


class HasherPasswordImp(HasherPassword):
    _pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def verify_password(self, raw_password, hashed_password):
        return self._pwd_context.verify(raw_password, hashed_password)

    def hash(self, password):
        return self._pwd_context.hash(password)