from flask import request, jsonify, current_app, render_template
from datetime import datetime

import sqlalchemy
from app.models.user_model import User
from app.configs.database import db
from flask_jwt_extended import create_access_token, jwt_required


def cadastrar_user():
    try:

        if request.method == 'GET':
            return render_template('cadastro.html')

        if request.method == 'POST':
            
            data = request.form

            new_user = {
                "user_name": data["name"],
                "user_birthdate": data["birthdate"],
                "user_cpf": data["cpf"],
                "user_city": data["cidade"],
                "user_phone": data["telefone"],
                "password": data["senha"]
            }

            user = User(**new_user)
            db.session.add(user)
            db.session.commit()

            if data:
                return render_template('login.html')

            return 'OLa'

        # return jsonify(user), 201
    except sqlalchemy.exc.IntegrityError:
        return {"msg": "Check the user data and try again. Read the documentation for more information."}, 400


# @jwt_required()
def get_users():
    # users = User.query.all()

    users = jsonify(json_list = User.query.all())

    print(users)

    return render_template('users.html')

    # return {"data":
    #     [serializer(user) for user in users]
    # }, 200


def login_user():
    data = request.json

    try:
        if request.method == 'GET':
            return render_template('login.html')

        # user = User.query.filter_by(user_cpf=data.get("user_cpf")).first()

        # if user.check_password(data.get('password')):
        #     access_token = create_access_token(user)
        #     return {"access_token": access_token}, 200

        # return {"msg": "Bad username or password."}, 401
    except AttributeError:
        return {"msg": "User with this cpf not found!"}, 404


# @jwt_required()
def delete_user():
    try:
        data = request.get_json()
        user = User.query.filter_by(id=data['id']).one()

        session = current_app.db.session
        session.delete(user)
        session.commit()

        return '', 204
    except KeyError:
        return {'message': 'Invalid key'}, 404


# @jwt_required()
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