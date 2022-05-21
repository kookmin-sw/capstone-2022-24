"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os.path
from datetime import timedelta
from pathlib import Path

import environ

# web
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent  # web
BACKEND_DIR = BASE_DIR.parent
ENV_DIR = os.path.join(BACKEND_DIR, "environment")

# read environment file
env = environ.Env(DEBUG=(bool, True))
environ.Env.read_env(env_file=os.path.join(ENV_DIR, ".env"))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Application definition

CUSTOM_APPS = [
    "users",
    "accounts",
    "applies",
    "wishes",
    "fellows",
    "group_accounts",
    "groups",
    "mileages",
    "movie_details",
    "notifications",
    "payments",
    "providers",
    "recent_views",
    "remittances",
    "star_ratings",
    "video_casts",
    "videos",
    "video_providers",
    "video_total_counts",
    "watching_marks",
    "tv_details",
    "mypages",
    "reports",
]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.sites",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # static/media file storages
    "storages",
    # django-rest-framework
    "rest_framework",
    "rest_framework.authtoken",
    # api documentation
    "drf_spectacular",
    # jwt: json web token
    "rest_framework_simplejwt.token_blacklist",
    # dj-rest-auth
    "dj_rest_auth",
    "dj_rest_auth.registration",
    # django-allauth
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.naver",
    "allauth.socialaccount.providers.google",
    # cors
    "corsheaders",
    # useful extentions
    "django_extensions",
    # for debugging
    "debug_toolbar",
    # auto one-to-one object create
    "annoying",
] + CUSTOM_APPS

REST_FRAMEWORK = {
    # camel case converter
    "DEFAULT_RENDERER_CLASSES": (
        "djangorestframework_camel_case.render.CamelCaseJSONRenderer",
        "djangorestframework_camel_case.render.CamelCaseBrowsableAPIRenderer",
    ),
    "DEFAULT_PARSER_CLASSES": (
        "djangorestframework_camel_case.parser.CamelCaseJSONParser",
        "djangorestframework_camel_case.parser.CamelCaseFormParser",
        "djangorestframework_camel_case.parser.CamelCaseMultiPartParser",
    ),
    "JSON_UNDERSCOREIZE": {
        "no_underscore_before_number": True,
    },
    # API document automation: drf-spectacular
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    # Permit only to authenticated user
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_AUTHENTICATION_CLASSES": ("rest_framework_simplejwt.authentication.JWTAuthentication",),
    # time stamp format
    "DATETIME_FORMAT": "%Y-%m-%d %H:%M:%S",
    "DATE_FORMAT": "%Y-%m-%d",
    "TIME_FORMAT": "%H:%M:%S",
}

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",  # cors
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",  # debug toolbar
    "django.middleware.locale.LocaleMiddleware",  # i18n
    "django.middleware.common.CommonMiddleware",
    "config.middleware.csrf.DisableCSRF",  # csrf disable (temporary)
    # "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

USE_I18N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BACKEND_DIR, "static/")  # caution

# Media files
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BACKEND_DIR, "media/")  # caution

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LANGUAGE_CODE = "ko-kr"

# CORS
CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_METHODS = (
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
)

CORS_ALLOW_HEADERS = [
    "accept",
    "host",
    "x-real-ip",
    "x-forwarded-for",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "location",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]

# SSL settings
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = True

# user model
AUTH_USER_MODEL = "users.User"

# API document automation (drf-spectacular)
SPECTACULAR_SETTINGS = {
    "TITLE": "온갖(Ongot) API",
    "DESCRIPTION": "[다학제간캡스톤디자인I] 24조",
    "CONTACT": {
        "name": "팀 뫄뫄",
        "url": "https://github.com/kookmin-sw/capstone-2022-24",
        "email": "kmu.sw.cap.2022@gmail.com",
    },
    "VERSION": "0.0.1",
    "SERVE_INCLUDE_SCHEMA": False,
    # list of authentication/permission classes for spectacular's views.
    "SERVE_PERMISSIONS": ["rest_framework.permissions.AllowAny"],
    # None will default to DRF's AUTHENTICATION_CLASSES
    "SERVE_AUTHENTICATION": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    # Initialize SwaggerUI with additional OAuth2 configuration.
    # https://swagger.io/docs/open-source-tools/swagger-ui/usage/oauth2/
    "SWAGGER_UI_OAUTH2_CONFIG": {},
    # Postprocessing functions that run at the end of schema generation.
    # must satisfy interface result = hook(generator, request, public, result)
    "POSTPROCESSING_HOOKS": ["drf_spectacular.hooks.postprocess_schema_enums"],
    # Preprocessing functions that run before schema generation.
    # must satisfy interface result = hook(endpoints=result) where result
    # is a list of Tuples (path, path_regex, method, callback).
    "PREPROCESSING_HOOKS": [],
    # Determines how operations should be sorted. If you intend to do sorting with a
    # PREPROCESSING_HOOKS, be sure to disable this setting. If configured, the sorting
    # is applied after the PREPROCESSING_HOOKS. Accepts either
    # True (drf-spectacular's alpha-sorter), False, or a callable for sort's key arg.
    "SORT_OPERATIONS": True,
    # Camelize names like operationId and path parameter names
    "CAMELIZE_NAMES": False,
    # Runs exemplary schema generation and emits warnings as part of "./manage.py check --deploy"
    "ENABLE_DJANGO_DEPLOY_CHECK": True,
    # TODO
    # Optional list of servers.
    "SERVERS": [
        {"url": "http://localhost:80/", "description": "Local server"},
        {"url": "https://development.server.link.todo/", "description": "Development server"},
        {"url": "https://main.server.link.todo/", "description": "Main server"},
    ],
    # Tags defined in the global scope
    "TAGS": [
        {"name": "Priority-1", "description": "1순위 API"},
        {"name": "Priority-2", "description": "2순위 API"},
        {"name": "Priority-3", "description": "3순위 API"},
        {"name": "Priority-4", "description": "4순위 API"},
        {"name": "User", "description": "사용자 API"},
        {"name": "Group", "description": "모임 API"},
        {"name": "Video", "description": "작품 API"},
        {"name": "Deprecated", "description": "설계만 반영"},
    ],
    # TODO
    # Oauth2 related settings. used for example by django-oauth2-toolkit.
    # https://spec.openapis.org/oas/v3.0.3#oauthFlowsObject
    "OAUTH2_FLOWS": [],
    "OAUTH2_AUTHORIZATION_URL": None,
    "OAUTH2_TOKEN_URL": None,
    "OAUTH2_REFRESH_URL": None,
    "OAUTH2_SCOPES": None,
    "SWAGGER_UI_SETTINGS": {
        "dom_id": "#swagger-ui",  # required(default)
        "layout": "BaseLayout",  # required(default)
        "filter": True,
        "deepLinking": True,
        "persistAuthorization": True,
        "displayOperationId": True,
    },
    "DISABLE_ERRORS_AND_WARNINGS": True,
}

# i18n
LANGUAGE_CODE = "ko"

LANGUAGES = [
    ("ko", "Korean"),
    ("en-us", "English"),
]

LOCALE_PATHS = [os.path.join(BACKEND_DIR, "locale")]  # src/back-end/locale

# auth
SITE_ID = 1
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USER_MODEL_USERNAME_FIELD = "nickname"
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_SIGNUP_REDIRECT_URL = "/register/"
ACCOUNT_EMAIL_VERIFICATION = "none"
LOGIN_REDIRECT_URL = "/"
STATE = env("STATE")

# oauth
SOCIALACCOUNT_ADAPTER = "users.adapter.UserAdapter"
SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "APP": {
            "client_id": env("OAUTH_GOOGLE_CLIENT_ID"),
            "secret": env("OAUTH_GOOGLE_SECRET"),
            "key": env("OAUTH_GOOGLE_API_KEY"),
        },
        "SCOPE": [
            "https://www.googleapis.com/auth/userinfo.email",
            "https://www.googleapis.com/auth/userinfo.profile",
            "https://www.googleapis.com/auth/user.birthday.read",
            "https://www.googleapis.com/auth/user.phonenumbers.read",
        ],
        "UTH_PARAMS": {
            "access_type": "online",
        },
    },
    "naver": {
        "APP": {
            "client_id": env("OAUTH_NAVER_CLIENT_ID"),
            "secret": env("OAUTH_NAVER_SECRET"),
            "key": "",
        },
        "SCOPE": ["name", "email", "birthyear", "mobile"],
    },
}

# jwt
REST_USE_JWT = True
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(hours=2),
    "REFRESH_TOKEN_LIFETIME": timedelta(hours=6),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": True,
}
JWT_AUTH_COOKIE = "ongot-token"
JWT_AUTH_REFRESH_COOKIE = "ongot-refresh-token"
USER_ID_FIELD = "nickname"

REST_AUTH_SERIALIZERS = {
    "LOGIN_SERIALIZER": "users.serializers.UserLoginSerializer",
    "REGISTER_SERIALIZER": "users.serializers.UserSignUpSerializer",
    "USER_DETAILS_SERIALIZER": "users.serializers.UserSerializer",
}

AUTHENTICATION_BACKENDS = {
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
}
