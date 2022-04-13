# How to write dotenv file
Fill in the values

## Local environment
`.env.local`
```dotenv
# common
BASE=
CRAWLER=
DB=
NGINX=
WEB=
STATIC=
MEDIA=
ENV=

# mongo
DB_USER=
DB_PASSWORD=
DB_HOST_NAME=
DB_HOST=
DB_NAME=
DB_PORT=
DB_ENFORCE_SCHEMA=

# web
WEB_DOCKERNAME=
WEB_PORT=
WEB_HOST=

# django
SECRET_KEY=

# uvicorn
MODULE_NAME=
VARIABLE_NAME=
GUNICORN_CONFIG=
SETTINGS_MODULE=

# aws s3
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_STORAGE_BUCKET_NAME=
AWS_S3_REGION_NAME=
AWS_S3_SECURE_URLS=
AWS_QUERY_STRING_AUTH=
AWS_S3_URL=
AWS_DEFAULT_ACL=
STATIC_LOCATION=
MEDIA_LOCATION=
```

### As of
2022.04.05 TUE