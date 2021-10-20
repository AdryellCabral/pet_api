from datetime import datetime
from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy import Column, Integer, DateTime, String


@dataclass
class AdoptionsModel(db.Model):
    id: int
    pet_info: str
    owner_info: str
    pet_name: str

    __tablename__ = "adoptions"

    id = Column(Integer, primary_key=True)

    created_at = Column(DateTime, nullable=False, default=datetime.today())

    pet_info = db.relationship("PetsModel", backref=db.backref("pet",
                               uselist=False))
    pet_id = db.Column(db.Integer, db.ForeignKey("pets.id"), nullable=False, unique=True)

    owner_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    owner_info = db.relationship("User", backref=db.backref("user", uselist=False))

    pet_name = db.Column(String(60), nullable=False)
