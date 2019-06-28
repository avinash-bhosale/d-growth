from d_growth import app, db
from d_growth.models import User, GrowthDetails
from flask import Blueprint, send_file, g, request, jsonify, url_for


api_blueprint = Blueprint('apis', __name__)


@api_blueprint.route("/api/users", methods=['GET', 'POST'])
def api_users():
    """ Creating new user and getting all users"""
    data = []
    if request.method == 'POST':
        appstruct = {}
        if request.json:
            appstruct = request.json
        elif request.form:
            appstruct = request.form.to_dict()
        new_user = User(appstruct)
        db.session.add(new_user)
        db.session.commit()
    else:
        users = User.query.all()
        data = [{"id": user.id, "name": user.name, "gender": user.gender, "dob": user.dob.strftime("%Y-%m-%d")} for user
                in users]
    return jsonify({'status': 'Success', 'data': data}), 200


@api_blueprint.route("/api/users/<user_id>", methods=['GET', 'PUT', 'DELETE'])
def api_user(user_id):
    """Updating existing user and deleting and getting all growths"""

    return jsonify({}), 200


@api_blueprint.route("/api/users/<user_id>/growths", methods=['GET', 'POST', 'DELETE'])
def api_user_growths(user_id):
    """ Adding user growths and removing"""
    data = []
    if request.method == 'POST':
        appstruct = {}
        if request.json:
            appstruct = request.json
        elif request.form:
            appstruct = request.form.to_dict()
        appstruct['user_id'] = user_id
        new_user = GrowthDetails(appstruct)
        db.session.add(new_user)
        db.session.commit()
        #
    else:
        growths = GrowthDetails.query.all()
        data = [{"id": growth.id, "height": growth.height, "weight": growth.weight, "date": growth.date.strftime("%Y-%m-%d")} for
                growth
                in growths]

    return jsonify({'status': 'Success', 'data': data}), 200
