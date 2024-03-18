import os


# ToDo: Fix the inheritance here - didn't want to lose too much time on thinking of use-cases
class BaseConfig:
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI', 'sqlite:///:memory:')
    SECRET_KEY = os.environ.get('SECRET_KEY')


class TestConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SECRET_KEY = 'SOMETHING_SECRET'
