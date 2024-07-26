from typing import List
from pydantic import Field
from datetime import datetime
from pydantic import BaseModel

from .base_schema import BaseSchema
from app.core.config import settings


class User(BaseSchema):
    nickname: str
    password: str
    age: int


class CreateUser(BaseSchema): ...


class UpdateUser(BaseSchema):
    nickname: str
    password: str
    age: int
    updated_at = Field(default_factory=datetime.now(settings.TIMEZONE))


class ListUsers(BaseModel):
    users: List[User]
