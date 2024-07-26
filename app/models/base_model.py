from datetime import datetime
from sqlmodel import SQLModel, Field

from app.main import brazil_tz


class BaseModel(SQLModel):
    created_at: datetime = Field(default_factory=datetime.now(brazil_tz))
    updated_at: datetime | None = None
