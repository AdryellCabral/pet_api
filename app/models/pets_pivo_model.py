from datetime import datetime
from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy import Column, Integer, DateTime, String


@dataclass
class PetPivoModel(db.Model):
    id: int
    pet_name: str
    pet_info: str

    __tablename__ = "pet_pivo"

    id = Column(Integer, primary_key=True)
    pet_name = Column(String(60), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.today())

    pet_info = db.relationship("PetsModel", backref=db.backref("pet",
                               uselist=False))
    pet_id = db.Column(db.Integer, db.ForeignKey("pets.id"), nullable=False)
