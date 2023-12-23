import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    db_host: str = os.getenv("DB_ADDRESS")
    db_user: str = os.getenv("DB_USER")
    db_port: str = os.getenv("DB_PORT")

settings = Settings()
