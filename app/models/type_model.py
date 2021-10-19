from datetime import datetime
from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy import Column, String, Integer


@dataclass
class Type(db.Model):
    id: int
    pet_type: str
    pet_race: str
    pet_size: str

    __tablename__ = "type"

    id = Column(Integer, primary_key=True)
    pet_type = Column(String(60), nullable=False)
    pet_race = Column(String(60), nullable=False)
    pet_size = Column(String(60), nullable=False)
