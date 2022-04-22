"""local settings file"""
# pylint: disable=R0801,W0401,W0614
import environ

from .base import *

env = environ.Env(DEBUG=(bool, False))

# read environment file
environ.Env.read_env(env_file=os.path.join(ENV_DIR, ".env.local"))

DEBUG = True

# SECURITY WARNING: don't run with debug turned on in production!
SECRET_KEY = env("SECRET_KEY")

ALLOWED_HOSTS = ["[::1]", "127.0.0.1", "localhost"]

# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": env("DB_NAME"),
        "USER": env("DB_USER"),
        "PASSWORD": env("DB_PASSWORD"),
        "HOST": env("DB_HOST_NAME"),
        "PORT": int(env("DB_PORT")),
        "TZ": env("TZ"),
        "OPTIONS": {"init_command": 'SET sql_mode="STRICT_TRANS_TABLES"'},
    }
}

# static / media location in WAS(not s3 on local environment)
STATIC_LOCATION = env("STATIC_LOCATION")
MEDIA_LOCATION = env("MEDIA_LOCATION")

# TZ
TIME_ZONE = env("TZ")
