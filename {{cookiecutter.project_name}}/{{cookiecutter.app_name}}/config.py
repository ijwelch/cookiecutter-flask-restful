"""Default configuration

Use env variables to override
"""
from flask_env import MetaFlaskEnv

class Configuration(metaclass=MetaFlaskEnv):
    DEBUG = True
    SECRET_KEY = "changeme"

    # SQLALCHEMY_DATABASE_URI = "mysql+pymysql://<USERNAME>:<PASSWORD>@<HOST>:<PORT>/<DB_NAME>"
    SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/{{cookiecutter.app_name}}.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']
