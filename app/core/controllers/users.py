from sqlalchemy.orm import Session

from core.db.schemas import User
from core.db.repositories import UsersRepository
from core.exceptions import EmailExistsException, InvalidPasswordConfirmException, PasswordLengthException


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

    new_user = User(email=email)
    new_user.set_password(password)
    UsersRepository.save(db, new_user)
    return new_user    
