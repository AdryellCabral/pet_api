from flask import Blueprint
from app.controllers.pets_pivo_controller import post_pet, get_all, delete_data, patch_data


bp = Blueprint("pets_pivo", __name__, url_prefix="/pet")

bp.post("")(post_pet)
bp.get("")(get_all)
bp.delete("")(delete_data)
bp.patch('')(patch_data)
