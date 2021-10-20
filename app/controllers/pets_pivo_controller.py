from flask import current_app, jsonify, request
from app.models.pets_pivo_model import PetPivoModel
from app.exc.exc_pet import NoDataFound
from sqlalchemy.exc import IntegrityError, NoResultFound
from sqlalchemy.orm.exc import DetachedInstanceError
from app.models.pet_model import PetsModel

# from flask_jwt_extended import jwt_required


# @jwt_required()
def post_pet():
    try:
        session = current_app.db.session

        data = request.get_json()

        select_pet = PetsModel.query.filter_by(id=data["pet_id"]).one()

        data.pop("pet_id")
        data["pet_info"] = select_pet

        pet = PetPivoModel(**data)

        session.add(pet)
        session.commit()

        return jsonify(pet)
    except IntegrityError as e:
        return {"Error": str(e.orig).split("\n")[0]}, 400


# @jwt_required()
def get_all():
    try:
        data = PetPivoModel.query.all()

        if data == []:
            raise NoDataFound

        return jsonify(data)
    except NoDataFound:
        return jsonify({"message": "No data found."}), 400


# @jwt_required()
def delete_data():
    try:
        session = current_app.db.session

        data = request.get_json()
        query = PetPivoModel.query.filter_by(id=data['id']).one()

        session.delete(query)
        session.commit()

        return "", 204
    except KeyError:
        return {'message': 'Invalid key'}, 404
    except NoResultFound:
        return {
            'message': 'No lines were found when one was needed'
            }, 404
    except DetachedInstanceError as e:
        return {
            'message': str(e)
            }, 404


# @jwt_required()
def patch_data():
    try:
        session = current_app.db.session
        data = request.get_json()

        query = PetPivoModel.query.filter_by(id=data['id']).one()

        for key, value in data.items():
            setattr(query, key, value)

        session.add(query)
        session.commit()

        return '', 204
    except KeyError:
        return {'message': 'Invalid'}, 404
    except AttributeError:
        return {'message': 'No data found.'}, 404


def select_data():
    try:
        data = request.get_json()

        query = PetPivoModel.query.filter_by(id=data['id']).one()

        return jsonify(query)

    except NoDataFound:
        return jsonify({"message": "No data found."}), 400
