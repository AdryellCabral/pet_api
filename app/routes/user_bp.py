from flask import Blueprint
from app.controllers.user_controller import cadastrar_user, get_users, login_user

bp_user = Blueprint("user", __name__)

bp_user.post("/signup")(cadastrar_user)
bp_user.get("/users")(get_users)
bp_user.post("/login")(login_user)
