from flask import Blueprint

bp_user = Blueprint("user", __name__)

@bp_user.get("/")
def first_route():
    return {"msg": "Hello world!"}, 200