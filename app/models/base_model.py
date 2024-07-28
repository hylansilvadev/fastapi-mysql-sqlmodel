from datetime import datetime
from uuid import uuid4
from sqlmodel import SQLModel, Field

from app.core.config import settings


class BaseModel(SQLModel):
    id: str = Field(default_factory=lambda: str(uuid4()), primary_key=True)
    created_at: datetime = Field(default_factory=lambda: datetime.now(settings.TIMEZONE))
    updated_at: datetime | None = None

    class Config:
        arbitrary_types_allowed = True