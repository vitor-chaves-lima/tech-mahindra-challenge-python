import datetime
import enum
import uuid
import bcrypt

from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer, String, Uuid, func, event
from sqlalchemy.orm import relationship

from . import Base


class UserRole(enum.Enum):
    admin = "admin"
    user = "user"

    def serialize(self):
        return self.value


class User(Base):
    __tablename__ = "users"

    id: uuid.UUID = Column(Uuid, primary_key=True, default=uuid.uuid4)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role =  Column(Enum(UserRole))
    created_at: datetime = Column(DateTime(timezone=True), default=func.now())
    updated_at: datetime = Column(DateTime(timezone=True), nullable=True)


    def set_password(self, password):
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')


    def check_password(self, password) -> bool:
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash.encode('utf-8'))


class PointEntry(Base):
    __tablename__ = "point_entries"

    id: uuid.UUID = Column(Uuid, primary_key=True, default=uuid.uuid4)
    amount: int = Column(Integer, nullable=False)
    user_id: uuid.UUID = Column(ForeignKey('users.id'), nullable=False)
    created_at: datetime = Column(DateTime(timezone=True), default=func.now())

    user = relationship("User")


@event.listens_for(User.__table__, "after_create")
def initialize_companies_table(target, connection, **_):
    connection.execute(target.insert(), [
    {
        'email': 'admin@gmail.com',
        'password_hash':  bcrypt.hashpw('admin123456'.encode('utf-8'), bcrypt.gensalt()).decode('utf-8'),
        'role': 'admin',
    }
])
    