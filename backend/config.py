import os


class BaseConfig:
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI', 'sqlite:////tmp/test.db')


class DebugConfig:
    SQLALCHEMY_TRACK_MODIFICATIONS = True
