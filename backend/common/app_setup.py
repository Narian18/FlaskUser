from flask import Flask

from backend.api.blueprints.user_bp import user_bp


def register_app_blueprints(app: Flask):
    """All blueprints in the app will registered in this function"""
    app.register_blueprint(user_bp)
