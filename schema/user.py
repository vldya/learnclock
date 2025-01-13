from typing import Optional

from pydantic import BaseModel


class UserLoginSchema(BaseModel):
    user_id: int
    access_token: str


class UserCreateSchema(BaseModel):
    username: Optional[str] = None
    password: Optional[str] = None
    google_access_token: Optional[str]
    email: Optional[str]
    name: Optional[str]

