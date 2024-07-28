from datetime import datetime
from sqlmodel import Field

from .base_model import BaseModel
from app.core.config import settings


class UserModel(BaseModel, table=True):
    __tablename__ = "tb_users"

    nickname: str = Field(max_length=24)
    age: int = Field(gt=0, lt=120)
    hashed_password: str = Field(max_length=255)
    last_login: datetime = Field(default_factory=lambda: datetime.now(settings.TIMEZONE))
