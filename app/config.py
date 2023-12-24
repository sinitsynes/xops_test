import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    db_host: str = os.getenv("DB_ADDRESS")
    db_user: str = os.getenv("DB_USER")
    db_port: str = os.getenv("DB_PORT")
    db_password: str = os.getenv("DB_PASSWORD")
    db_name: str = os.getenv('DB_NAME')
    test_db_name: str = os.getenv('TEST_DB_NAME')

settings = Settings()
