from storages.backends.s3boto3 import S3Boto3Storage
from ..settings.local import AWS_STATIC_LOCATION, AWS_MEDIA_LOCATION


# static file storage
class StaticStorage(S3Boto3Storage):
    default_acl = None
    location = AWS_STATIC_LOCATION


# media file storage
class MediaStorage(S3Boto3Storage):
    default_acl = 'private'
    location = AWS_MEDIA_LOCATION
