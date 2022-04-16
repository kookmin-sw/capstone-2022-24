"""Video Total Counts App Model Serializer Definitions : VideoTotalCountSerialaizer"""
from rest_framework import serializers

from .models import VideoTotalCount


class VideoTotalCountSerialaizer(serializers.ModelSerializer):
    """Video total Count information Serializing to get data"""

    class Meta:
        """Video total Count Serializer field setting"""

        model = VideoTotalCount
        fields = ["videoId", "dibsCount", "watchCount", "viewCount"]
