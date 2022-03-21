"""development settings file"""
# pylint: disable=R0801,W0401,W0614
import environ

from .base import *

env = environ.Env(DEBUG=(bool, False))

# reading environment file
environ.Env.read_env(env_file=os.path.join(ENV_DIR, ".env.dev"))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

DEBUG = False

ALLOWED_HOSTS = [env("WEB_HOST"), "localhost"]

# Database

DATABASES = {
    "default": {
        "ENGINE": "djongo",
        "NAME": env("DB_NAME"),
        "ENFORCE_SCHEMA": env("DB_ENFORCE_SCHEMA"),
        'CLIENT': {
            'host': env('DB_HOST_NAME'),
            'port': int(env('DB_PORT')),
            'username': env('DB_USER'),
            'password': env('DB_PASSWORD'),
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
