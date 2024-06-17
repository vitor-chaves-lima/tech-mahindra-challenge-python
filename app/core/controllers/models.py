import uuid
from pydantic import BaseModel

from core.db.schemas import UserRole


class Tokens(BaseModel):
    refresh_token: str
    access_token: str
    access_token_expires_at: int

    class Config:
        frozen = True


class AccessToken(BaseModel):
    access_token: str
    access_token_expires_at: int

    class Config:
        frozen = True

    
class UserData(BaseModel):
    id: uuid.UUID
    email: str
    role: UserRole

    class Config:
        frozen = True