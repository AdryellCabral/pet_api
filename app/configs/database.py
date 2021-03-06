from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_app(app):
    db.init_app(app)
    app.db = db

    from app.models.user_model import User
    from app.models.adoptions_model import AdoptionsModel
    from app.models.pet_model import PetsModel
