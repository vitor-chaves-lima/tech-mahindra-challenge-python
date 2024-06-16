from sqlalchemy.orm import Session
from .schemas import User


class UsersRepository:
    @staticmethod
    def find_by_email(db: Session, email: str) -> User:
        return db.query(User).filter(User.email == email).first()


    @staticmethod
    def exists_by_email(db: Session, email: str) -> bool:
        return db.query(User).filter(User.email == email).first() is not None
    

    @staticmethod
    def save(db: Session, user: User) -> User:
        db.add(user)
        db.commit()
        return user