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


class Settings(BaseSettings):
    project_name: str = Field(..., env='PROJECT_NAME')
    log_level: bool = Field(..., env='LOG_LEVEL')
    host: str = Field(..., env='HOST')
    port: int = Field(..., env='HOST_BACKEND_PORT')

    postgres: PostgresSettings = PostgresSettings()
    postgres_url: str = postgres.dsn()

    class Config:
        env_file = 'app/.env'
        env_file_encoding = 'utf-8'