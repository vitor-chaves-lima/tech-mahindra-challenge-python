from typing import List
import uuid
from sqlalchemy.orm import Session

from core.db.schemas import PointEntry
from core.db.repositories import PointEntriesRepository, UsersRepository
from core.exceptions import EmailNotFoundException


def add_points_controller(db: Session, email: str, amount: int):
    user_exists = UsersRepository.exists_by_email(db, email)
    if user_exists is False:
        raise EmailNotFoundException(email)
    
    user = UsersRepository.find_by_email(db, email)
    PointEntriesRepository.save(db, PointEntry(amount=amount, user_id=user.id))


def get_user_points_controller(db: Session, user_id: uuid.UUID) -> List[PointEntry]:
    user_points = PointEntriesRepository.get_user_points(db, user_id)
    return user_points