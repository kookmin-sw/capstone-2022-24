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

    video = serializers.SerializerMethodField()

    def get_video(self, obj):
        """Method : get to Video data Using RatingSerializer"""

        return VideoSerializer(obj.video).data

    class Meta:
        """Metadata for video rating Serializer"""

        model = Rating
        fields = "__all__"


class ProductionCountrySerializer(serializers.ModelSerializer):
    """ProductionCountry model Serializer in videos application"""

    video = serializers.SerializerMethodField()

    def get_video(self, obj):
        """Method : get to Video data Using ProductionCountrySerializer"""

        return VideoSerializer(obj.video).data

    class Meta:
        """Metadata for video Production Country Serializer"""

        model = ProductionCountry
        fields = "__all__"


class GenreSerializer(serializers.ModelSerializer):
    """Genre model Serializer in videos application"""

    video = serializers.SerializerMethodField()

    def get_video(self, obj):
        """Method : get to Video data Using GerneSerializer"""

        return VideoSerializer(obj.video).data

    class Meta:
        """Metadata for video Gernes Serializer"""

        model = Genre
        fields = "__all__"


class VideoHistorySerializer(serializers.ModelSerializer):
    """Video summary histories in Mypage"""

    poster_url = serializers.URLField(source="poster_key", required=False)

    class Meta:
        """Metadata for video histories summary"""

        model = Video
        fields = ["id", "tmdb_id", "poster_url"]

        read_only_fields = ["__all__"]

class VideoListSerializer(serializers.ModelSerializer):
    """Video Lists information Serializing to get data"""

    poster_url = serializers.URLField(source="poster_key", required=False)

    class Meta:
        """Metadata for video histories summary"""

        model = Video
        fields = ["id", "title", "poster_url"]

        read_only_fields = ["__all__"]
