from storages.backends.s3boto3 import S3Boto3Storage
from .settings.base import STATIC_LOCATION, MEDIA_LOCATION


# static file storage
class StaticStorage(S3Boto3Storage):
    default_acl = 'public-read'
    location = STATIC_LOCATION


# media file storage
class MediaStorage(S3Boto3Storage):
    default_acl = 'private'
    location = MEDIA_LOCATION
