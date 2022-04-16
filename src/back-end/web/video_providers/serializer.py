"""Video Providers App Model Serializer Definitions : VideoProviderSerialaizer"""

from rest_framework import serializers

from .models import VideoProvider


class VideoProviderSerialaizer(serializers.ModelSerializer):
    """Video Providers information Serializing to get data"""

    class Meta:
        """Video Providers Serializer field setting"""

        model = VideoProvider
        fields = ["videoId", "offerType", "link", "offerDate", "deadline"]
