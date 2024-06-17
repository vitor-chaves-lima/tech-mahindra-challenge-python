from sqlalchemy.orm import Session

from core.controllers.models import AccessToken, Tokens
from core.controllers.tokens import create_access_token, create_refresh_token, validate_refresh_token
from core.db.schemas import User
from core.db.repositories import UsersRepository
from core.exceptions import EmailExistsException, EmailNotFoundException, InvalidPasswordConfirmException, PasswordLengthException, InvalidCredentialsException


def sign_up_controller(db: Session, email: str, password: str, password_confirm: str) -> User:
    password_length = len(password)
    password_confirm_length = len(password)

    if password_length < 8 or password_confirm_length < 8:
        raise PasswordLengthException(password_confirm_length)
    
    if password != password_confirm:
        raise InvalidPasswordConfirmException()

    email_exists = UsersRepository.exists_by_email(db, email)
    if email_exists is True:
        raise EmailExistsException(email)

    new_user = User(email=email, role="user")
    new_user.set_password(password)
    UsersRepository.save(db, new_user)
    return new_user    


def sign_in_controller(db: Session, email: str, password: str) -> Tokens:
    password_length = len(password)

    if password_length < 8:
        raise PasswordLengthException(password_length)
    

    email_exists = UsersRepository.exists_by_email(db, email)
    if email_exists is False:
        raise EmailNotFoundException(email)

    user = UsersRepository.find_by_email(db, email)
    
    valid_credentials = user.check_password(password)
    if valid_credentials is False:
        raise InvalidCredentialsException()
    
    refresh_token = create_refresh_token({"id": f"{user.id}", "email": user.email, "role": user.role.serialize()})
    access_token = create_access_token({"id": f"{user.id}", "email": user.email, "role": user.role.serialize()})
    access_token_expire = 900

    return Tokens(refresh_token=refresh_token, 
                  access_token=access_token, 
                  access_token_expires_at=access_token_expire)


def refresh_token_controller(refresh_token: str) -> AccessToken:
    validate_refresh_token(refresh_token)

    access_token = create_access_token()
    access_token_expire = 900

    return AccessToken(access_token=access_token, access_token_expires_at=access_token_expire)
