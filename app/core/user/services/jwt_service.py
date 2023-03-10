from app.core.user.protocols.jwt_service import JwtService
import jwt
from app.settings import Settings


class JwtServiceImp(JwtService):

    settings = Settings()

    def encode(self, payload: dict) -> str:
        return jwt.encode(
            payload,
            self.settings.secret,
            algorithm=self.settings.jwr_algorithm,
        )

    def decode(self, token: str) -> dict:
        return jwt.decode(
            token,
            self.settings.secret,
            algorithms=[self.settings.jwr_algorithm]
        )
