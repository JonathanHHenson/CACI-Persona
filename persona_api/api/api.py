from flask import Blueprint, jsonify, request
from persona_api.db import db_operations
from persona_api.db.utils import jsonify_one, jsonify_list

blueprint = Blueprint('api', __name__)


@blueprint.route('/search/<string:username>', methods=['GET'])
def get_person(username):
    person = db_operations.get_person(username)
    if person:
        return jsonify_one(person), 200
    else:
        return jsonify({
            'message': f'Person with username=\'{username}\' could not be found'
        }), 404


@blueprint.route('/people', methods=['GET'])
def get_people():
    # Get the top and skip query args and clamp them
    top = max(1, min(1000, int(request.args.get('top', default=50))))
    skip = max(0, int(request.args.get('skip', default=0)))

    return jsonify_list(db_operations.get_people(top, skip))


@blueprint.route('/people/<string:username>', methods=['DELETE'])
def delete_person(username):
    person = db_operations.get_person(username)
    if person:
        db_operations.delete_person(person)
        return '', 204
    else:
        return jsonify({
            'message': f'Person with username=\'{username}\' could not be deleted because the person could not be found'
        }), 404
