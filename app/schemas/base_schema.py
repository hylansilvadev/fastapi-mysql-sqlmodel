import uuid
from pydantic import BaseModel, UUID4, Field
from datetime import datetime

from app.core.config import settings


class BaseSchema(BaseModel):
    id: UUID4 = Field(default_factory=uuid.uuid4())
    created_at: datetime = Field(default_factory=datetime.now(settings.TIMEZONE))
    updated_at: datetime | None = None
