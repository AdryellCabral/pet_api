from flask import Blueprint
from app.controllers.pet_controller import post_pet, get_all, delete_data

bp = Blueprint("pet", __name__, url_prefix="/pet")

bp.post("")(post_pet)
bp.get("")(get_all)
bp.delete("")(delete_data)