import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


def make_dsn():
    host = os.getenv("DB_ADDRESS")
    user = os.getenv("DB_USER")
    port = os.getenv("DB_PORT")
    return f"postgresql+asyncpg://{user}@{host}:{port}/xops_test"


class Settings(BaseSettings):
    postgres_dsn: str = make_dsn()
    db_echo: bool = False


settings = Settings()
