from flask import Flask, render_template

from backend.config import BaseConfig
from backend.common.app_setup import register_app_blueprints
from backend.common.login import login_manager


def create_app(config=BaseConfig):
    from backend.common.db import db
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    login_manager.init_app(app)

    register_app_blueprints(app)

    # ToDo: Remove
    @app.route('/')
    def index():
        return render_template('index.html', username='TestUsername')

    return app


app = create_app()
