from typing import List
import uuid
from sqlalchemy.orm import Session
from .schemas import PointEntry, User


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
    

class PointEntriesRepository:
    @staticmethod
    def save(db: Session, point_entry: PointEntry) -> User:
        db.add(point_entry)
        db.commit()
        return point_entry
    

    def get_user_points(db: Session, user_id: uuid.UUID) -> List[PointEntry]:
        return db.query(PointEntry).filter(PointEntry.user_id == user_id).all()