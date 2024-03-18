from flask import Blueprint
from flask_login import login_required


user_bp = Blueprint('users', __name__)


@user_bp.route('/login', methods=["POST"])
def login_route():
    from backend.api.services.user_service import login
    return login()


@user_bp.route('/logout')
@login_required
def logout_route():
    from backend.api.services.user_service import logout
    return logout()
