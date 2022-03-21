"""local settings file"""
# pylint: disable=R0801,W0401,W0614
import environ

from .base import *

env = environ.Env(DEBUG=(bool, False))

# Read environment.local file
environ.Env.read_env(env_file=os.path.join(ENV_DIR, '.env.local'))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')
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
