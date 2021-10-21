from flask import Blueprint
from app.controllers.user_controller import cadastrar_user, get_users, login_user, delete_user, update_user

bp_user = Blueprint("user", __name__, url_prefix="/api/users")

bp_user.get("/signup")(cadastrar_user)
bp_user.post("/signup")(cadastrar_user)
bp_user.get("/login")(login_user)
bp_user.post("/login")(login_user)
bp_user.get("")(get_users)
bp_user.delete("")(delete_user) # os dados do usuario a ser deletado estao no body
bp_user.patch("")(update_user)
