#!/usr/bin/env sh
set -eu

envsubst '${APP_HOST} ${APP_PORT} ${APP_LOCATION}' < /etc/nginx/conf.d/default.conf.template > /etc/nginx/conf.d/default.conf
exec "$@"
