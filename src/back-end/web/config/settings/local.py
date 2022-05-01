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

# static / media location in WAS(not s3 on local environment)
STATIC_LOCATION = env("STATIC_LOCATION")
MEDIA_LOCATION = env("MEDIA_LOCATION")

ALLOWED_HOSTS = ["[::1]", "127.0.0.1", "localhost"]

# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": env("DB_NAME"),
        "USER": env("DB_USER"),
        "PASSWORD": env("DB_PASSWORD"),
        "HOST": env("DB_HOST"),
        "PORT": int(env("DB_PORT")),
        "TZ": env("TZ"),
        "OPTIONS": {"init_command": 'SET sql_mode="STRICT_TRANS_TABLES"'},
    }
}
"""
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": 'ongotdb',
        "USER": 'root',
        "PASSWORD": 'root',
        "HOST": '127.0.0.1',
        "PORT": 3306,
        "TZ": 'Asia/Seoul',
        "OPTIONS": {"init_command": 'SET sql_mode="STRICT_TRANS_TABLES"'},
    }
}
"""
# Cache
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f"redis://:{env('CACHE_PASSWORD')}@{env('CACHE_HOST')}:{env('CACHE_PORT')}/1",
        "OPTIONS": {"CLIENT_CLASS": "django_redis.client.DefaultClient", "PASSWORD": env("CACHE_PASSWORD")},
    }
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"
CACHE_TTL = 60 * 1  # example: @method_decorator(cache_page(CACHE_TTL))

# TZ
TIME_ZONE = env("TZ")

# celery: async task queue
# CELERY_BROKER_URL = f"amqp://{env('BROKER_HOST_NAME')}@{env('BROKER_PASSWORD')}:{env('BROKER_PORT')}/0"
