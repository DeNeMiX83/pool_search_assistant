from pydantic import (
    BaseSettings, Field
)

env_file_path = 'deploy/.env'


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
        env_file = env_file_path
        env_file_encoding = 'utf-8'


class RedisSettings(BaseSettings):
    host: str = Field(..., env='REDIS_HOST')
    port: int = Field(..., env='REDIS_PORT')
    db: int = Field(..., env='REDIS_DB')

    def dsn(self) -> str:
        return f'redis://{self.host}:{self.port}/{self.db}'

    class Config:
        env_file = env_file_path
        env_file_encoding = 'utf-8'


class MosApiSettings(BaseSettings):
    mos_api_key: str = Field(..., env='MOS_API_KEY')
    mos_api_url: str = Field(..., env='MOS_API_URL')
    mos_api_dataset_id: int = Field(..., env='MOS_API_DATASET_ID')

    def get_mos_api_dataset_url(self) -> str:
        return f'{self.mos_api_url}/{self.mos_api_dataset_id}'

    class Config:
        env_file = env_file_path
        env_file_encoding = 'utf-8'


class Settings(BaseSettings):
    project_name: str = Field(..., env='PROJECT_NAME')
    log_level: str = Field(..., env='LOG_LEVEL')
    host: str = Field(..., env='HOST')
    port: int = Field(..., env='HOST_BACKEND_PORT')
    secret: str = Field(..., env='SECRET')
    root_path: str = Field(..., env='ROOT_PATH')

    api_url: str = Field(..., env='API_URL')
    docs_url: str = Field(..., env='DOCS_URL')

    postgres: PostgresSettings = PostgresSettings()
    postgres_url: str = postgres.dsn()

    redis: RedisSettings = RedisSettings()

    jwr_algorithm: str = Field(..., env='JWT_ALGORITHM')
    password_algorithm: str = Field(..., env='PASSWORD_ALGORITHM')

    mos_api: MosApiSettings = MosApiSettings()

    class Config:
        env_file = env_file_path
        env_file_encoding = 'utf-8'
