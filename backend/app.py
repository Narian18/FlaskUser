from flask import Flask, render_template

from backend.config import BaseConfig
from backend.utils.app_setup import register_app_blueprints


def create_app(config=BaseConfig):
    from backend.utils.db import db
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)

    register_app_blueprints(app)
    return app


app = create_app()


@app.route('/')
def index():
    return render_template('index.html', username='TestUsername')
