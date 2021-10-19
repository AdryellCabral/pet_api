from datetime import datetime
from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime


@dataclass
class PetModel(db.Model):
    id: int
    pet_name: str
    pet_description: str
    pet_localization: str
    pet_birthdate: datetime
    created_at: datetime

    __tablename__ = "pet"

    id = Column(Integer, primary_key=True)
    pet_name = Column(String(60), nullable=False)
    pet_birthdate = Column(DateTime, nullable=False)
    pet_description = Column(String(155), nullable=False, unique=True)
    pet_localization = Column(String(60), nullable=False)
    created_at = Column(DateTime, nullable=False)
    # type_id = Column(Integer, ForeignKey("type.id"), nullable=False,
    #                  unique=True)
