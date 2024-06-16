from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from api.models import ErrorMessage, SignUpUserRequestPayload, UserResponse
from core.controllers.users import sign_up_controller
from core.db import get_db


api_router = APIRouter(prefix="/api")


@api_router.post("/auth/sign-in", status_code=status.HTTP_200_OK)
async def sign_in(db: Session = Depends(get_db)):
    ...


@api_router.post("/auth/sign-up", 
                 status_code=status.HTTP_201_CREATED, 
                 response_model=UserResponse,
                 responses={400: {"model": ErrorMessage}})
async def sign_up(request: SignUpUserRequestPayload, db: Session = Depends(get_db)):
    email = request.email
    password = request.password
    
    new_user = sign_up_controller(db, email, password)
    return new_user


@api_router.post("/auth/refresh", status_code=status.HTTP_200_OK)
async def refresh_token(db: Session = Depends(get_db)):
    ...