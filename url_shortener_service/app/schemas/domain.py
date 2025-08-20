from datetime import datetime, timezone
import uuid
from pydantic import EmailStr
from sqlmodel import Field, SQLModel


class UserBase(SQLModel):
    username: str = Field(index=True, unique=True, max_length=50)
    email: EmailStr = Field(index=True, unique=True, max_length=255)
    is_active: bool = Field(default=True)
    is_superuser: bool = Field(default=False)


class UserCreate(UserBase):
    password: str = Field(min_length=8, max_length=40)


class UserRegister(SQLModel):
    username: str = Field(max_length=50)
    email: str = Field(max_length=255)
    password: str = Field(min_length=8, max_length=40)


class UserId(SQLModel):
    id: uuid.UUID


class UserPublicShort(SQLModel):
    id: uuid.UUID
    username: str


class UserPublic(UserBase):
    id: uuid.UUID
    followers: list[UserPublicShort] = []
    followees: list[UserPublicShort] = []


class UsersPublic(SQLModel):
    users: list[UserPublic]
    count: int


class TokenPayload(SQLModel):
    sub: str | None = None


class Token(SQLModel):
    access_token: str


class ShortURLCreate(SQLModel):
    url: str
    created_at: datetime = Field(default_factory=datetime.now)


class ShortURL(ShortURLCreate):
    short_code: str = Field(index=True, unique=True)
    expires_at: datetime = Field()
