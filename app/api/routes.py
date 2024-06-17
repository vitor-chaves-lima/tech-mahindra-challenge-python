from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from api.models import ErrorMessage, SignInUserRequestPayload, SignUpUserRequestPayload, TokensResponse, UserResponse
from core.controllers.users import sign_up_controller, sign_in_controller
from core.db import get_db


api_router = APIRouter(prefix="/api")


@api_router.post("/auth/sign-up", 
                 status_code=status.HTTP_201_CREATED, 
                 response_model=UserResponse,
                 responses={400: {"model": ErrorMessage}})
async def sign_up(request: SignUpUserRequestPayload, db: Session = Depends(get_db)):
    email = request.email
    password = request.password
    password_confirm = request.password_confirm
    
    new_user = sign_up_controller(db, email, password, password_confirm)
    return new_user


@api_router.post("/auth/sign-in", 
                 status_code=status.HTTP_200_OK, 
                 response_model=TokensResponse,
                 responses={400: {"model": ErrorMessage}})
async def sign_in(request: SignInUserRequestPayload, db: Session = Depends(get_db)):
    email = request.email
    password = request.password

    tokens = sign_in_controller(db, email, password)
    return tokens


@api_router.post("/auth/refresh", status_code=status.HTTP_200_OK)
async def refresh_token(db: Session = Depends(get_db)):
    ...