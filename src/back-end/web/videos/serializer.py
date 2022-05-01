"""Videos App Model Serializer: Video, VideoDetail"""
from rest_framework import serializers
from videos.models import Gerne, ProductionCountry, Rating, Video, VideoDetail


class VideoSerialaizer(serializers.ModelSerializer):
    """Video model Serializer in videos application"""

    class Meta:
        """Metadata for videos Serializer"""

        model = Video
        fields = "__all__"


class VideoDetailSerialaizer(serializers.ModelSerializer):
    """VideoDetail model Serializer in videos application"""

    video = serializers.SerializerMethodField()

    def get_video(self, obj):
        """Method : get to Video data Using VideosDetailsSerialaizer"""
        return VideoSerialaizer(obj.video).data

    class Meta:
        """Metadata for videos details Serializer"""

        model = VideoDetail
        fields = "__all__"


class RatingSerializer(serializers.ModelSerializer):
    """Rating model Serializer in videos application"""

    video_details = serializers.SerializerMethodField()

    def get_video_detail(self, obj):
        """Method : get to Video detail data Using RatingSerializer"""

        return VideoDetailSerialaizer(obj.video_details).data

    class Meta:
        """Metadata for video rating Serializer"""

        model = Rating
        fields = "__all__"


class ProductionCountrySerializer(serializers.ModelSerializer):
    """ProductionCountry model Serializer in videos application"""

    video_details = serializers.SerializerMethodField()

    def get_video_detail(self, obj):
        """Method : get to Video detail data Using ProductionCountrySerializer"""

        return VideoDetailSerialaizer(obj.video_details).data

    class Meta:
        """Metadata for video Production Country Serializer"""

        model = ProductionCountry
        fields = "__all__"


class GernesSerializer(serializers.ModelSerializer):
    """VideoDetail model Serializer in videos application"""

    video_details = serializers.SerializerMethodField()

    def get_video_detail(self, obj):
        """Method : get to Video detail data Using GernesSerializer"""

        return VideoDetailSerialaizer(obj.video_details).data

    class Meta:
        """Metadata for video Gernes Serializer"""

        model = Gerne
        fields = "__all__"
