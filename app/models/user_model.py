from datetime import datetime
from sqlalchemy.sql.expression import false
from sqlalchemy.sql.sqltypes import DateTime
from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy import Column, String, Integer, DateTime, Boolean
from werkzeug.security import generate_password_hash, check_password_hash

@dataclass
class User(db.Model):
    id: int
    user_name: str
    user_birthdate: datetime
    user_phone: str
    user_city: str
    created_at: datetime

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    user_name = Column(String(60), nullable=False)
    user_birthdate = Column(DateTime, nullable=False)
    user_cpf = Column(String, nullable=False, unique=True)
    user_city = Column(String, nullable=False)
    is_owner = Column(Boolean, default=bool(false))
    user_phone = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now())
    last_modified = Column(DateTime, nullable=True)
    password_hash = Column(String(511), nullable=False)

    @property
    def password(self):
        raise AssertionError('Password is not accessible.')

    @password.setter
    def password(self, password_to_hash):
        self.password_hash = generate_password_hash(password_to_hash)

    def check_password(self, password_to_compare):
        is_valid_password = check_password_hash(self.password_hash, password_to_compare)
        return is_valid_password
