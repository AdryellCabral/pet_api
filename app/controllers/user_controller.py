from flask import request, jsonify
from datetime import datetime
from app.models.user_model import User
from app.configs.database import db


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