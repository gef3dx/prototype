# app/core/config.py
from pydantic_settings import BaseSettings, SettingsConfigDict



class Settings(BaseSettings):
    DATABASE_URL: str
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings(DATABASE_URL="db.sqlite3")
