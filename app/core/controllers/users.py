from sqlalchemy.orm import Session

from core.db.schemas import User
from core.db.repositories import UsersRepository
from core.exceptions import EmailExistsException, PasswordLengthException


def sign_up_controller(db: Session, email: str, password: str) -> User:
    email_exists = UsersRepository.exists_by_email(db, email)
    password_length = len(password)

    if email_exists is True:
        raise EmailExistsException(email)
    
    if password_length < 8:
        raise PasswordLengthException(password_length)
    

    new_user = User(email=email)
    new_user.set_password(password)
    UsersRepository.save(db, new_user)
    return new_user    
