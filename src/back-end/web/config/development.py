"""development settings file"""
# pylint: disable=R0801,W0401,W0614
import environ

from .settings import *

env = environ.Env(DEBUG=(bool, False))

# reading .env file
environ.Env.read_env(env_file=os.path.join(BASE_DIR, ".env.dev"))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

DEBUG = False

ALLOWED_HOSTS = ["*"]

# Database

DATABASES = {
    "default": {
        "ENGINE": "djongo",
        "NAME": env("DB_NAME"),
        "ENFORCE_SCHEMA": env("DB_ENFORCE_SCHEMA"),
        "CLIENT": {
            "HOST": env("DB_HOST"),
            "PORT": env("DB_PORT"),
            "USERNAME": env("DB_USER"),
            "PASSWORD": env("DB_PASSWORD"),
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
