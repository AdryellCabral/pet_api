from flask import Blueprint
from app.controllers.pet_controller import post_pet, get_all, delete_data, patch_data, filter_by_city


bp = Blueprint("pet", __name__, url_prefix="/pet")

bp.post("")(post_pet)
bp.get("")(get_all)
bp.delete("")(delete_data)
bp.patch('')(patch_data)
bp.get('/localization')(filter_by_city)
