from flask import Blueprint
from app.controllers.adoptions_controller import adotar_pet, post_pet, get_all, delete_data, patch_data


bp = Blueprint("pets_pivo", __name__, url_prefix="/api/adoptions")

bp.post("")(post_pet)
bp.get("")(get_all)
bp.delete("")(delete_data)
bp.patch('')(patch_data)
bp.post("/new")(adotar_pet)
