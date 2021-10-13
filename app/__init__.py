from flask import Flask
from app import routes
from app.configs import env_configs, database, migration, jwt


def create_app():
    
    app = Flask(__name__)

    env_configs.init_app(app)
    database.init_app(app)
    migration.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(routes.bp)
    
    return app
