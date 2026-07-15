from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application configuration loaded from environment variables or `.env`."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False,
    )

    app_name: str = "Tri9T AI CT-200 Backend"
    environment: str = "development"
    database_url: str = "sqlite:///./ct200.db"

    mongo_uri: str | None = None
    mongo_database: str = "ct200_generations"

    llm_provider: str | None = None
    llm_api_key: str | None = Field(default=None, repr=False)
    llm_model: str | None = None


@lru_cache
def get_settings() -> Settings:
    """Return one settings instance per process."""
    return Settings()
