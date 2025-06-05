
from pydantic_settings import BaseSettings
# config.py
DEBUG_MODE = True
EXPIRE_DELTA = 30

class Settings(BaseSettings):
    MONGO_DB_NAME:str
    COLLECTION_CLIENT:str
    MONGO_URI:str
    SECRET_KEY:str
    ALGORITHM:str

    class Config:
        env_file = ".env"

settings = Settings()



