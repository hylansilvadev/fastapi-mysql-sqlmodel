import uuid
from datetime import datetime
from sqlmodel import Field

from .base_model import BaseModel
from app.main import brazil_tz


class UserModel(BaseModel, table=True):
    __tablename__ = "tb_users"

    id: uuid
    nickname: str = Field(max_length=24)
    ag: int = Field(gt=0, lt=120)
    hashed_password: str = Field(max_length=255)
    last_login: datetime = Field(default_factory=datetime.now(brazil_tz))
