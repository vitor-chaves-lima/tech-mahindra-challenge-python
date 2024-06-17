from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from core.db.schemas import UserRole
from core.controllers.models import UserData
from core.exceptions import InvalidUserRoleException
from core.controllers.tokens import validate_access_token

auth_scheme = HTTPBearer()


def validate_token(token: HTTPAuthorizationCredentials = Depends(auth_scheme)) -> UserData:
    return validate_access_token(token.credentials)


def check_user_role(user_data: UserData = Depends(validate_token)) -> UserData:
    print(user_data.role)
    if(user_data.role != UserRole.user):
        raise InvalidUserRoleException(UserRole.user, user_data.role)
    
    return user_data