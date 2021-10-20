from flask import Blueprint
from app.controllers.pets_controller import create_type, get_all, delete_data, patch_data, select_data


bp = Blueprint("list_pet", __name__, url_prefix="/api/pets")

bp.post("")(create_type)
bp.get("")(get_all)
bp.delete("")(delete_data)
bp.patch("")(patch_data)
bp.post("/select-pet")(select_data)
