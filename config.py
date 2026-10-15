import os
from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    PROJECT_NAME: str = "PlacePulse AI"
    VERSION: str = "1.0.0"
    API_PREFIX: str = "/api"
    DATABASE_URL: str = "sqlite:///./placepulse.db"
    
    # AI Config
    GEMINI_API_KEY: Optional[str] = os.getenv("GEMINI_API_KEY", "")
    GEMINI_MODEL: str = "gemini-1.5-flash"
    
    # Admin Security
    ADMIN_TOKEN: str = os.getenv("ADMIN_TOKEN", "admin123")
    
    class Config:
        env_file = ".env"
        extra = "allow"

settings = Settings()
