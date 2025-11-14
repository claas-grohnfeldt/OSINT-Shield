from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application configuration using environment variables for overrides."""

    env: str = "dev"
    database_url: str = "sqlite+aiosqlite:///./osint_shield.db"
    frontend_origin: str = "http://localhost:5173"

    model_config = SettingsConfigDict(
        env_prefix="OSINT_SHIELD_",
        env_file=".env",
        extra="ignore",
    )


settings = Settings()
