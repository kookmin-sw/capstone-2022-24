"""Serializers of videos application for json parsing : VideoSerializer, VideoProviderSerialaizer, RatingSerializer,
                                                        GenreSerialaizer, ProductionCountrySerialaizer"""
from rest_framework import serializers
from videos.models import Genre, ProductionCountry, Rating, Video, VideoDetail


class VideoSerializer(serializers.ModelSerializer):
    """Video model Serializer in videos application"""

    class Meta:
        """Metadata for videos Serializer"""

        model = Video
        fields = "__all__"


class VideoDetailSerializer(serializers.ModelSerializer):
    """VideoDetail model Serializer in videos application"""

    video = serializers.SerializerMethodField()

    def get_video(self, obj):
        """Method : get to Video data Using VideosDetailsSerialaizer"""
        return VideoSerializer(obj.video).data

    class Meta:
        """Metadata for videos details Serializer"""

        model = VideoDetail
        fields = "__all__"


class RatingSerializer(serializers.ModelSerializer):
    """Rating model Serializer in videos application"""

    video_details = serializers.SerializerMethodField()

    def get_video_detail(self, obj):
        """Method : get to Video detail data Using RatingSerializer"""

        return VideoDetailSerializer(obj.video_details).data

    class Meta:
        """Metadata for video rating Serializer"""

        model = Rating
        fields = "__all__"


class ProductionCountrySerializer(serializers.ModelSerializer):
    """ProductionCountry model Serializer in videos application"""

    video_details = serializers.SerializerMethodField()

    def get_video_detail(self, obj):
        """Method : get to Video detail data Using ProductionCountrySerializer"""

        return VideoDetailSerializer(obj.video_details).data

    class Meta:
        """Metadata for video Production Country Serializer"""

        model = ProductionCountry
        fields = "__all__"


class GenreSerializer(serializers.ModelSerializer):
    """Genre model Serializer in videos application"""

    video_details = serializers.SerializerMethodField()

    def get_video_detail(self, obj):
        """Method : get to Video detail data Using GerneSerializer"""

        return VideoDetailSerializer(obj.video_details).data

    class Meta:
        """Metadata for video Gernes Serializer"""

        model = Genre
        fields = "__all__"
