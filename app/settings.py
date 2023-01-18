from pydantic import (
    BaseSettings, Field
)


class PostgresSettings(BaseSettings):
    host: str = Field(..., env='POSTGRES_HOST')
    port: int = Field(..., env='POSTGRES_PORT')
    user: str = Field(..., env='POSTGRES_USER')
    password: str = Field(..., env='POSTGRES_PASSWORD')
    database: str = Field(..., env='POSTGRES_DB')

    def dsn(self) -> str:
        return "{scheme}://{user}:{password}@{host}/{db}".format(
            scheme="postgresql+asyncpg",
            user=self.user,
            password=self.password,
            host=self.host,
            db=self.database,
        )


    class Config:
        env_file = 'app/.env'
        env_file_encoding = 'utf-8'


class TokenSettings(BaseSettings):
    secret: str = Field(..., env='SECRET')
    algorithm: str = Field(..., env='JWT_ALGORITHM')
    access_token_expire_minutes: int = Field(..., env='ACCESS_TOKEN_EXPIRE_MINUTES')
    refresh_token_expire_minutes: int = Field(..., env='REFRESH_TOKEN_EXPIRE_MINUTES')
    

    class Config:
        env_file = 'app/.env'
        env_file_encoding = 'utf-8'


class Settings(BaseSettings):
    project_name: str = Field(..., env='PROJECT_NAME')
    log_level: bool = Field(..., env='LOG_LEVEL')
    host: str = Field(..., env='HOST')
    port: int = Field(..., env='HOST_BACKEND_PORT')

    postgres: PostgresSettings = PostgresSettings()
    postgres_url: str = postgres.dsn()

    token: TokenSettings = TokenSettings()

    class Config:
        env_file = 'app/.env'
        env_file_encoding = 'utf-8'