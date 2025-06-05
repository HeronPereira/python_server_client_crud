
import os
from pydantic_settings import BaseSettings
# config.py
DEBUG_MODE = True
EXPIRE_DELTA = 30

BASE_URL = os.getenv("BASE_URL", "http://127.0.0.1:8000")


class Settings(BaseSettings):
    MONGO_DB_NAME:str
    COLLECTION_CLIENT:str
    MONGO_URI:str
    SECRET_KEY:str
    ALGORITHM:str

    class Config:
        env_file = ".env"

settings = Settings()



