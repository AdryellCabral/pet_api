from flask import request, jsonify
from datetime import datetime
from app.models.user_model import User
from app.configs.database import db
from flask_jwt_extended import create_access_token, jwt_required


def serializer(obj):
    return {
        "name": obj.user_name,
        "id": obj.id,
        "birthdate": obj.user_birthdate
    }


def cadastrar_user():
    data = request.json
    data["created_at"] = datetime.now()

    user = User(**data)

    db.session.add(user)
    db.session.commit()

    return jsonify(user), 201
    
def get_users():
    users = User.query.all()

    return {"data": 
        [serializer(user) for user in users]
    }, 200


def login_user():
    data = request.json

    try:
        user = User.query.filter_by(user_cpf=data.get("user_cpf")).first()

        if user.check_password(data.get('password')):
            access_token = create_access_token(user)
            return {"access_token": access_token}, 200
        
        return {"msg": "Bad username or password."}, 401
    except AttributeError:
        return {"msg": "User with this cpf not found!"}, 404
