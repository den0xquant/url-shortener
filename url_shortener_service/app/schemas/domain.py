from datetime import datetime
from pydantic import BaseModel, Field


class ShortURLCreate(BaseModel):
    long_url: str
    created_at: datetime = Field(default_factory=datetime.now)


class ShortURL(ShortURLCreate):
    short_code: str = Field()
    expires_at: datetime
