from datetime import datetime, date
from sqlmodel import Field

from .base_model import BaseModel
from app.core.config import settings


class UserModel(BaseModel, table=True):
    __tablename__ = "tb_users"

    nickname: str = Field(max_length=24)
    hashed_password: str = Field(max_length=255)
    email: str = Field(max_length=45)
    last_login: datetime = Field(default_factory=lambda: datetime.now(settings.TIMEZONE))
    first_name: str = Field(max_length=24, default=None)
    last_name: str = Field(max_length=24, default=None)
    image_url: str = Field(max_length=255, default=None)
    birth_date: date = Field(default=None)

    
    