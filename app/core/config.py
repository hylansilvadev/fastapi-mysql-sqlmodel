from pydantic_settings import BaseSettings, SettingsConfigDict
from pytz import timezone
import secrets


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_ignore_empty=True
    )

    # DATABASE_CONNECTRION
    DATABASE_TYPE: str
    CONNECTOR: str
    USERNAME: str
    PASSWORD: str
    PORT: int
    HOST: str
    DATABASE: str

    # SECURITY_API
    SECRET_KEY: str = secrets.token_hex(32)
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    @property
    def DATABASE_URL(self) -> str:
        return f"{self.DATABASE_TYPE}+{self.CONNECTOR}://{self.USERNAME}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.DATABASE}"

    @property
    def TIMEZONE(self):
        return timezone('America/Sao_Paulo')


settings = Settings()
