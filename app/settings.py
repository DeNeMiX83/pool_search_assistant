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


class MosApiSettings(BaseSettings):
    mos_api_key: str = Field(..., env='MOS_API_KEY')
    mos_api_url: str = Field(..., env='MOS_API_URL')
    mos_api_dataset_id: int = Field(..., env='MOS_API_DATASET_ID')

    def get_mos_api_dataset_url(self) -> str:
        return f'{self.mos_api_url}/{self.mos_api_dataset_id}'

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

    mos_api: MosApiSettings = MosApiSettings()



    class Config:
        env_file = 'app/.env'
        env_file_encoding = 'utf-8'