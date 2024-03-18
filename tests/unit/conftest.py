import pytest

from backend.app import create_app
from backend.config import TestConfig
from backend.common.db import db


@pytest.fixture()
def app():
    app = create_app()
    app.config.from_object(TestConfig)
    with app.app_context():
        db.create_all()
        yield app

        db.session.remove()
        db.drop_all()


@pytest.fixture()
def client(app):
    return app.test_client()
