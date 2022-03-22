"""development settings file"""
# pylint: disable=R0801,W0401,W0614
import environ

from .base import *

env = environ.Env(DEBUG=(bool, False))

# reading environment file
# environ.Env.read_env(env_file=os.path.join(ENV_DIR, ".env.dev"))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = False

ALLOWED_HOSTS = [os.getenv("WEB_HOST"), "localhost"]

# Database

DATABASES = {
    "default": {
        "ENGINE": "djongo",
        "NAME": os.getenv("DB_NAME"),
        "ENFORCE_SCHEMA": os.getenv("DB_ENFORCE_SCHEMA"),
        'CLIENT': {
            'host': os.getenv('DB_HOST_NAME'),
            'port': os.getenv('DB_PORT', 27017),
            'username': os.getenv('DB_USER'),
            'password': os.getenv('DB_PASSWORD'),
            'authSource': 'admin',
            'authMechanism': 'SCRAM-SHA-1',
        },
        "LOGGING": {
            "version": 1,
            "loggers": {
                "djongo": {
                    "level": "DEBUG",
                    "propagate": False,
                }
            },
        },
    }
}
