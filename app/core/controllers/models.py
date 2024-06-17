from pydantic import BaseModel


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