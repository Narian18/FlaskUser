from flask import Blueprint
from flask_login import login_required

from backend.api.schemas.user_schemas import LoginSchema, LoginRequest
from backend.common.api_validators import json_args

user_bp = Blueprint('users', __name__)


@user_bp.route('/login', methods=["POST"])
@json_args(LoginSchema())
def login_route(request: LoginRequest):
    from backend.api.services.user_service import login
    return login(request.username, request.password)


@user_bp.route('/logout')
@login_required
def logout_route():
    from backend.api.services.user_service import logout
    return logout()
