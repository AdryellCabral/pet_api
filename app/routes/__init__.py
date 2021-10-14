from flask import Flask

def init_app(app: Flask):
    from app.routes.user_bp import bp_user
    app.register_blueprint(bp_user)