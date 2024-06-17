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