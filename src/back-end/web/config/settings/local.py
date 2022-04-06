"""local settings file"""
# pylint: disable=R0801,W0401,W0614
import environ

from .base import *

env = environ.Env(DEBUG=(bool, False))

# read environment file
environ.Env.read_env(env_file=os.path.join(ENV_DIR, '.env.local'))

DEBUG = True

# SECURITY WARNING: don't run with debug turned on in production!
SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = ['[::1]', '127.0.0.1', 'localhost']

# Database

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': env('DB_NAME'),
        'ENFORCE_SCHEMA': env('DB_ENFORCE_SCHEMA'),
        'CLIENT': {
            'host': env('DB_HOST_NAME'),
            'port': int(env('DB_PORT')),
            'username': env('DB_USER'),
            'password': env('DB_PASSWORD'),
            'authSource': 'admin',
            'authMechanism': 'SCRAM-SHA-1',
        },
        'LOGGING': {
            'version': 1,
            'loggers': {
                'djongo': {
                    'level': 'DEBUG',
                    'propagate': False,
                }
            },
        },
    }
}

# static / media location in WAS(not s3 on local environment)
STATIC_LOCATION = env("STATIC_LOCATION")
MEDIA_LOCATION = env("MEDIA_LOCATION")
