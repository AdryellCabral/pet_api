from flask import Flask


def init_app(app: Flask):
    from app.routes.user_bp import bp_user
    app.register_blueprint(bp_user)

    from app.routes.pets_bp import bp as bp_pet
    app.register_blueprint(bp_pet)

    from .adoptions_bp import bp as bp_type_pet
    app.register_blueprint(bp_type_pet)
