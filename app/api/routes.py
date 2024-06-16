from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from core.db import get_db


api_router = APIRouter(prefix="/api")


@api_router.post("/auth/sign-in", status_code=status.HTTP_200_OK)
async def sign_in(db: Session = Depends(get_db)):
    ...


@api_router.post("/auth/sign-up", status_code=status.HTTP_200_OK)
async def sign_in(db: Session = Depends(get_db)):
    ...


@api_router.post("/auth/refresh", status_code=status.HTTP_200_OK)
async def sign_in(db: Session = Depends(get_db)):
    ...