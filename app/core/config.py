from pydantic_settings import BaseSettings, SettingsConfigDict
from pytz import timezone


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_ignore_empty=True
    )
    
    DATABASE_TYPE: str
    CONNECTOR: str
    USERNAME: str
    PASSWORD: str
    PORT: int
    HOST: str
    DATABASE: str
    
    @property
    def DATABASE_URL(self) -> str:
        return f"{self.DATABASE_TYPE}+{self.CONNECTOR}://{self.USERNAME}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.DATABASE}"
    
    @property
    def TIMEZONE(self):
        return timezone('America/Sao_Paulo')
        


settings = Settings()