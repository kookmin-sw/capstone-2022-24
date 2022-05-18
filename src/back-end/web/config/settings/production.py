"""production settings file"""
# pylint: disable=R0801,W0401,W0614
from .base import *

env = environ.Env(DEBUG=(bool, False))

# read environment file
environ.Env.read_env(env_file=os.path.join(ENV_DIR, ".env.prod"))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

DEBUG = False

ALLOWED_HOSTS = [env("WEB_HOST"), env("WEB_DNS"), "localhost"]

# static / media storage
DEFAULT_FILE_STORAGE = "config.storages.production.MediaStorage"
STATICFILES_STORAGE = "config.storages.production.StaticStorage"

# static / media location in s3
STATIC_LOCATION = env("STATIC_LOCATION")
MEDIA_LOCATION = env("MEDIA_LOCATION")

# aws s3
AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = env("AWS_STORAGE_BUCKET_NAME")
AWS_S3_SECURE_URLS = env("AWS_S3_SECURE_URLS")
AWS_QUERY_STRING_AUTH = env("AWS_QUERY_STRING_AUTH")
AWS_DEFAULT_ACL = env("AWS_DEFAULT_ACL")

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

# Cache
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f"redis://{env('CACHE_HOST')}@{env('CACHE_PASSWORD')}:{env('CACHE_PORT')}/1",
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

# app
APP_PORT = env("APP_PORT")
APP_HOST = env("APP_HOST")

# base url
WEB_URL = env("WEB_URL")

# cors
CORS_ORIGIN_WHITELIST = [
    f"http://localhost:{env('APP_PORT')}",
    f"http://127.0.0.1:{env('APP_PORT')}",
    f"http://{env('APP_HOST')}:{env('APP_PORT')}",
]

# video api key
API_KEY_V3 = env("MOVIE_API_KEY_V3")

# static / media storage
AWS_S3_CUSTOM_DOMAIN = env("AWS_S3_CUSTOM_DOMAIN")

# debug toolbar
if DEBUG:
    import os  # only if you haven't already imported this
    import socket  # only if you haven't already imported this

    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [ip[: ip.rfind(".")] + ".1" for ip in ips] + ["127.0.0.1", "10.0.2.2"]
    DEBUG_TOOLBAR_CONFIG = {"SHOW_TOOLBAR_CALLBACK": lambda _request: DEBUG}
