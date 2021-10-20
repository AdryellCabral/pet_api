from flask import request, jsonify, current_app, render_template
from datetime import datetime

import sqlalchemy
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
    try:
        data = request.json

        data["created_at"] = datetime.now()

        user = User(**data)

        db.session.add(user)
        db.session.commit()

        return jsonify(user), 201
    except sqlalchemy.exc.IntegrityError:
        return {"msg": "Check the user data and try again. Read the documentation for more information."}, 400
    
def get_users():

    #TODO: Melhorar a forma de serializar esses dados, o jsonify nao funciona

    users = User.query.all()

    return render_template('users.html', users=users)

    # return {"data":
    #     [serializer(user) for user in users]
    # }, 200


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


@jwt_required()
def delete_user():
    try:
        data = request.get_json()
        user = User.query.filter_by(id=data['id']).one()

        session = current_app.db.session
        session.delete(user)
        session.commit()

        return jsonify(user), 204
    except KeyError:
        return {'message': 'Invalid key'}, 404


@jwt_required()
def update_user():
    try:
        session = current_app.db.session
        data = request.get_json()

        user = User.query.filter_by(id=data['id']).one()

        for key, value in data.items():
            setattr(user, key, value)

        session.add(user)
        session.commit()

        return '', 204
        
    except KeyError:
        return {'message': 'Invalid'}, 404
    except AttributeError:
        return {'message': 'No data found.'}, 404