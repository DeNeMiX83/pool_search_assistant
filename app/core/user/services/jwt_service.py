from app.core.user.protocols.jwt_service import JwtService
import jwt
from app.settings import TokenSettings


class JwtServiceImp(JwtService):

    settings = TokenSettings()

    def encode(self, payload: dict) -> str:
        return jwt.encode(
            payload, 
            self.settings.secret, 
            algorithm=self.settings.algorithm,
        )

    def decode(self, token: str) -> dict:
        return jwt.decode(
            token, 
            self.settings.secret, 
            algorithm=self.settings.algorithm
        )