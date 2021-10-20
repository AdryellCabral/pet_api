from flask import Blueprint
from app.controllers.pets_controller import create_type, get_all, delete_data, patch_data


bp = Blueprint("list_pet", __name__, url_prefix="/pet/list")

bp.post("")(create_type)
bp.get("")(get_all)
bp.delete("")(delete_data)
bp.patch("")(patch_data)
