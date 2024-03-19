from http import HTTPStatus

from backend.models.user import User
from backend.common.db import db


USERNAME = 'Foo'
EMAIL = 'Foo'
PASSWORD = 'Foo'


def create_test_user():
    """ requires app context """
    new_user: User = User(name=USERNAME, email=EMAIL)
    new_user.set_password(PASSWORD)
    db.session.add(new_user)
    db.session.commit()

    return new_user


def test_user_get_methods(app):
    with app.app_context():
        new_user = create_test_user()

        assert User.get_by_name(new_user.name) == new_user
        assert User.get_by_id(new_user.id) == new_user


def test_login_logout(app, client):
    with app.app_context():
        create_test_user()

    response = client.post('/login', json={'username': USERNAME, 'password': PASSWORD})
    assert response.status_code == HTTPStatus.OK, response.json

    response = client.get('/logout')
    assert response.status_code == HTTPStatus.NO_CONTENT

    response = client.post('/login', json={'username': EMAIL, 'password': PASSWORD})
    assert response.status_code == HTTPStatus.OK
    # second logout ensures email also logged you in
    response = client.get('/logout')
    assert response.status_code == HTTPStatus.NO_CONTENT


def test_login_logout_errors(app, client):
    with app.app_context():
        create_test_user()

    err_uname_missing = "'username': ['Missing data for required field.']"
    err_pword_missing = "'password': ['Missing data for required field.']"
    response = client.post("/login", json={})
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json == {"error": f'{{{err_uname_missing}, {err_pword_missing}}}'}, response.json

    response = client.post("/login", json={"username": USERNAME})
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json == {"error": f'{{{err_pword_missing}}}'}, response.json

    response = client.post("/login", json={"password": PASSWORD})
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json == {"error": f'{{{err_uname_missing}}}'}, response.json

    response = client.post("/login", json={"username": "WrongName", "password": PASSWORD})
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json == {"error": f'No user found for name or email "WrongName"'}, response.json

    response = client.post("/login", json={"username": USERNAME, "password": "WrongPassword"})
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json == {"error": f'Incorrect password for user "{USERNAME}"'}, response.json
