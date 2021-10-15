from datetime import datetime
from flask.scaffold import F
from sqlalchemy.sql.expression import null
from sqlalchemy.sql.sqltypes import DateTime
from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, Boolean

@dataclass
class User(db.Model):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    user_name = Column(String(60), nullable=False)
    user_birthdate = Column(DateTime, nullable=False)
    user_cpf = Column(String, nullable=False, unique=True)
    user_city = Column(String, nullable=False)
    is_owner = Column(Boolean, nullable=False)
    user_phone = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)
    last_modified = Column(DateTime, nullable=True)
    #pet_id = Column(Integer, ForeignKey("pet.id"), nullable=False, unique=True)
