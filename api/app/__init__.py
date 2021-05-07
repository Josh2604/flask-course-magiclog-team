import logging.config
from os import environ
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
# App configuration
from .config import config as app_config
# Entrypoint
from api.entrypoints.handlers.api.user import user


def create_app():
    load_dotenv()
    APPLICATION_ENV = get_environment()
    logging.config.dictConfig(app_config[APPLICATION_ENV].LOGGING)
    app = Flask(app_config[APPLICATION_ENV].APP_NAME)
    app.config.from_object(app_config[APPLICATION_ENV])

    CORS(app, resources={r'/api/*': {'origins': '*'}})

    app.register_blueprint(user)

    return app


def get_environment():
    return environ.get('APPLICATION_ENV') or 'development'
