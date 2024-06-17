from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from api.models import AddPointsRequestPayload, ErrorMessage, GetUserPointsResponse, RefreshRequestPayload, RefreshResponse, SignInUserRequestPayload, SignUpUserRequestPayload, SignInResponse, UserPointEntry, UserResponse
from api.utils import check_admin_role, check_user_role
from core.controllers.models import UserData
from core.controllers.points import add_points_controller, get_user_points_controller
from core.controllers.auth import refresh_token_controller, sign_up_controller, sign_in_controller
from core.db import get_db


api_router = APIRouter(prefix="/api")


@api_router.post("/auth/sign-up", 
                 status_code=status.HTTP_201_CREATED, 
                 response_model=UserResponse,
                 responses={400: {"model": ErrorMessage}},
                 tags=["Auth"])
async def sign_up(request: SignUpUserRequestPayload, db: Session = Depends(get_db)):
    email = request.email
    password = request.password
    password_confirm = request.password_confirm
    
    new_user = sign_up_controller(db, email, password, password_confirm)
    return new_user


@api_router.post("/auth/sign-in", 
                 status_code=status.HTTP_200_OK, 
                 response_model=SignInResponse,
                 responses={400: {"model": ErrorMessage}},
                 tags=["Auth"])
async def sign_in(request: SignInUserRequestPayload, db: Session = Depends(get_db)):
    email = request.email
    password = request.password

    tokens = sign_in_controller(db, email, password)
    return tokens


@api_router.post("/auth/refresh", 
                 status_code=status.HTTP_200_OK, 
                 response_model=RefreshResponse,
                 responses={400: {"model": ErrorMessage}},
                 tags=["Auth"])
async def refresh_access_token(request: RefreshRequestPayload):
    refresh_token = request.refresh_token

    access_token = refresh_token_controller(refresh_token)
    return access_token


@api_router.post("/points", 
                 status_code=status.HTTP_201_CREATED, 
                 responses={400: {"model": ErrorMessage}},
                 tags=["Points"])
async def add_points(request: AddPointsRequestPayload, 
                     db: Session = Depends(get_db),
                     _: UserData = Depends(check_admin_role)):
    user_email = request.user_email
    amount = request.amount

    add_points_controller(db, user_email, amount)


@api_router.get("/points", 
                 status_code=status.HTTP_200_OK, 
                 tags=["Points"])
async def get_points(db: Session = Depends(get_db), user_data: UserData = Depends(check_user_role)):
    user_id = user_data.id
    user_points = get_user_points_controller(db, user_id=user_id)

    user_points_response: List[UserPointEntry] = []

    for point in user_points:
        response_point = UserPointEntry(id=point.id, amount=point.amount, created_at=point.created_at)
        user_points_response.append(response_point)

    return GetUserPointsResponse(data=user_points_response)
    