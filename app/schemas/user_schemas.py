from typing import Optional
from datetime import datetime, date
from pydantic import BaseModel, EmailStr
from uuid import UUID


class User(BaseModel):
    nickname: str
    password: str
    email: EmailStr
    first_name: str | None = None
    last_name: str | None = None
    image_url: str | None = None
    birth_date: date | None = None


class CreateUser(BaseModel):
    nickname: str
    email: EmailStr
    password: str


class UpdateUser(BaseModel):
    nickname: Optional[str]
    password: Optional[str]
    email: Optional[EmailStr]
    first_name: Optional[str]
    last_name: Optional[str]
    image_url: Optional[str]
    birth_date: Optional[date]


class UserResponse(BaseModel):
    id: UUID
    nickname: str
    hashed_password: str
    email: EmailStr | None = None
    first_name: str | None = None
    last_name: str | None = None
    image_url: str | None = None
    birth_date: date | None = None
    last_login: datetime
    created_at: datetime
    updated_at: datetime | None
