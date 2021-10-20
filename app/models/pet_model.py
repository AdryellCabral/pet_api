from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime


@dataclass
class PetsModel(db.Model):
    id: int
    pet_type: str
    pet_race: str
    pet_size: str
    pet_birthdate: datetime
    pet_description: str
    pet_localization: str

    __tablename__ = "pets"

    id = Column(Integer, primary_key=True)
    pet_type = Column(String(60), nullable=False)
    pet_race = Column(String(60), nullable=False)
    pet_size = Column(String(60), nullable=False)
    pet_birthdate = Column(DateTime, nullable=False)
    pet_description = Column(String(155), nullable=False)
    pet_localization = Column(String(60), nullable=False)
