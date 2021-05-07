from os import path, environ
from dotenv import load_dotenv

basedir = path.abspath(path.join(path.dirname(__file__), "../../"))

load_dotenv()


class BaseConfig(object):
    APP_NAME = environ.get("APP_NAME") or "flask_app"
    ORIGINS = ['*']
    EMAIL_CHARSET = "UTF-8"
    API_KEY = environ.get("API_KEY")
    BROKER_URL = environ.get("BROKER_URL")
    LOG_INFO_FILE = path.join(basedir, "log", "info.log")

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'standard': {
                'format': '[%(asctime)s] - %(name)s - %(levelname)s - '
                          '%(message)s',
                'datefmt': '%b %d %Y %H:%M:%S'
            },
            'simple': {
                'format': '%(levelname)s - %(message)s'
            },
        },
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'simple'
            },
            'log_info_file': {
                'level': 'DEBUG',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': LOG_INFO_FILE,
                'maxBytes': 16777216,  # 16megabytes
                'formatter': 'standard',
                'backupCount': 5
            },
        },
        'loggers': {
            APP_NAME: {
                'level': 'DEBUG',
                'handlers': ['log_info_file'],
            },
        },
    }


class Development(BaseConfig):
    DEBUG = True
    ENV = 'development'


class Staging(BaseConfig):
    DEBUG = True
    ENV = 'staging'


class Production(BaseConfig):
    DEBUG = False
    ENV = 'production'


config = {
    'production': Production,
    'development': Development,
    'staging': Staging,
}