from flask import current_app, jsonify, request
from app.models.pet_model import PetModel
from app.exc.exc_pet import NoDataFound


def post_pet():

    session = current_app.db.session
    data = request.get_json()

    pet = PetModel(**data)

    session.add(pet)
    session.commit()

    return {
        "id": pet.id,
        "pet_name": pet.pet_name,
        "pet_birthdate": pet.pet_birthdate,
        "pet_description": pet.pet_description,
        "pet_localization": pet.pet_localization,
        "created_at": pet.created_at,
        # "type_id": pet.type_id
    }, 201


def get_all():
    try:
        data = PetModel.query.all()

        if data == []:
            raise NoDataFound

        return jsonify(data)
    except NoDataFound:
        return jsonify({"message": "No data found."}), 400


def delete_data():
    try:
        data = request.get_json()
        query = PetModel.query.filter_by(
                                        pet_name=data['pet_name']).one()

        session = current_app.db.session
        session.delete(query)
        session.commit()

        return jsonify(query), 204
    except KeyError:
        return {'message': 'Invalid key'}, 404


def patch_data():
    try:
        session = current_app.db.session
        data = request.get_json()

        query = PetModel.query.filter_by(pet_name=data['pet_name']).one()

        for key, value in data.items():
            setattr(query, key, value)

        session.add(query)
        session.commit()

        return '', 204
    except KeyError:
        return {'message': 'Invalid'}, 404
    except AttributeError:
        return {'message': 'No data found.'}, 404
