from pydantic import BaseSettings
from functools import lru_cache
import os

class Settings(BaseSettings):
    db_host: str = os.environ.get('DB_HOST', 'localhost')
    db_name: str = os.environ.get('DB_NAME', 'dev')
    db_username: str = os.environ.get('DB_USERNAME', 'root')
    db_password: str = os.environ.get('DB_PASSWORD', 'example')


@lru_cache()
def get_settings():
    return Settings()
