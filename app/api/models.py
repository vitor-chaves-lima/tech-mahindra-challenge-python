from typing import Annotated, Union
from uuid import UUID
from pydantic import BaseModel, EmailStr, Field, StringConstraints
from datetime import datetime


class ErrorMessage(BaseModel):
    message: str
    error: str


class SignUpUserRequestPayload(BaseModel):
    email: EmailStr
    password: Annotated[str,StringConstraints(min_length=8)]


class UserResponse(BaseModel):
    id: UUID
    email: str
    createdAt: datetime = Field(alias="created_at")
    updatedAt: Union[datetime, None] = Field(alias="updated_at")

    class Config:
        from_attributes = True