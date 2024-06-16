from typing import Union
from uuid import UUID
from pydantic import BaseModel, Field
from datetime import datetime


class SignUpUserRequestPayload(BaseModel):
    email: str
    password: str

class UserResponse(BaseModel):
    id: UUID
    email: str
    createdAt: datetime = Field(alias="created_at")
    updatedAt: Union[datetime, None] = Field(alias="updated_at")

    class Config:
        from_attributes = True