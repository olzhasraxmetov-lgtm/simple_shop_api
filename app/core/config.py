from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    PROJECT_NAME: str = 'Simple shop API'
    PROJECT_VERSION: str = '0.1.0'
    PROJECT_DESCRIPTION: str = 'Simple shop API'

    SECRET_KEY: str = 'aa977d4fb25c6930f5ea42d06571d97ab0b261e1ae710fabe753cfa9e8eb0e28'
    ALGORITHM: str = "HS256"
    DATABASE_URL: str = "postgresql+asyncpg://simple_user:olzhas@localhost:5432/simple_shop_db"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()