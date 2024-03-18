from typing import Tuple, Dict

from flask import request
from flask_login import login_user
from http import HTTPStatus

from backend.common.errors import wrap_error
from backend.models.user import User


def login() -> Tuple[Dict[str, str], int]:
    request_json = request.get_json(silent=True)
    if not request_json or not request_json.get("username") or not request_json.get("password"):
        return wrap_error('Form Incomplete', HTTPStatus.BAD_REQUEST)

    name_or_email = request_json.get("username")
    password = request_json.get("password")

    user = User.get_by_name(name_or_email)
    if not user:
        user = User.get_by_email(name_or_email)
        if not user:
            return wrap_error(f"No user found for name or email \"{name_or_email}\"", HTTPStatus.BAD_REQUEST)

    if not user.check_password(password):
        return wrap_error(f"Incorrect password for user \"{name_or_email}\"", HTTPStatus.BAD_REQUEST)

    login_user(user)
    return {"message": "User Successfully logged in"}, HTTPStatus.OK


def logout() -> Tuple[Dict[str, str], int]:
    return {"message": "User Successfully logged out"}, HTTPStatus.NO_CONTENT
