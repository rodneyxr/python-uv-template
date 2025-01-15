from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    # DEBUG
    debug: bool = False


@lru_cache()
def get_settings() -> Settings:
    return Settings()