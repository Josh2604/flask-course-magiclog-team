from flask import Blueprint, jsonify
from api.core.usecases.show_users.show_users import UserCase
from api.decorators.auth import require_key, require_test

user = Blueprint('user', __name__, url_prefix='/api/v1/users')

@user.route('/')
def index():
    try:
        user_response = UserCase.show_users()
        response = {
            "code": 200,
            "data": user_response
        }
        return jsonify(response)
    except Exception as error:
        print(error)
        return jsonify({"code": 500, "message": "Error getting users"})


@user.route('/verify')
@require_test
@require_key
def verify():
    return jsonify({"message": "Autorizado"})