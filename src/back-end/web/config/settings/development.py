"""development settings file"""
# pylint: disable=R0801,W0401,W0614
import environ

from .base import *

env = environ.Env(DEBUG=(bool, False))

# read environment file
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

# aws s3
AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')
AWS_S3_SECURE_URLS = env('AWS_S3_SECURE_URLS')
AWS_QUERY_STRING_AUTH = env('AWS_QUERY_STRING_AUTH')
