from datetime import datetime
from pydantic import BaseModel
from uuid import UUID



class User(BaseModel):
    nickname: str
    password: str
    age: int


class CreateUser(User):
    class Config:
        orm_mode = True


class UpdateUser(BaseModel):
    nickname: str
    password: str
    age: int


class UserResponse(BaseModel):
    id: UUID
    nickname: str
    password: str
    age: int
    last_login: datetime
    created_at: datetime
    updated_at: datetime | None
