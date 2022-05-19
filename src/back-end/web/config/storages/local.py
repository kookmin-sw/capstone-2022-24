"""Settings about local storages of static/media files"""
# pylint: disable=W0223
from storages.backends.s3boto3 import S3Boto3Storage

from ..settings.local import MEDIA_LOCATION, STATIC_LOCATION

__all__ = (
    "StaticStorage",
    "MediaStorage",
)


# static file storage
class StaticStorage(S3Boto3Storage):
    """Static storage of local environment"""

    default_acl = None
    location = STATIC_LOCATION


# media file storage
class MediaStorage(S3Boto3Storage):
    """Media storage of local environment"""

    default_acl = "private"
    location = MEDIA_LOCATION
