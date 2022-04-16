"""Video Total Counts App Model Serializer Definitions : VideosSerialaizer"""
from rest_framework import serializers

from .models import VideoTotalCount


class VideosSerialaizer(serializers.ModelSerializer):
    """Video information Serializing to get data"""

    class Meta:
        """Video Serializer field setting"""

        model = VideoTotalCount
        fields = ["videoId", "dibsCount", "watchCount", "viewCount"]
