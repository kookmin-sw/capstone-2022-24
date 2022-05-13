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


class MyVideoTotalHistorySerializer(serializers.Serializer):
    """Mypage total video summary of user's histories"""

    def update(self, instance, validated_data):
        """Not used"""

    def create(self, validated_data):
        """Not usedd"""

    recent_views = serializers.SerializerMethodField(read_only=True)
    watch_marks = serializers.SerializerMethodField(read_only=True)
    wishes = serializers.SerializerMethodField(read_only=True)
    stars = serializers.SerializerMethodField(read_only=True)

    def get_recent_views(self, user):
        """Get user's recent view histories"""
        _queryset = Video.objects.prefetch_related("recentview_set__user").filter(recentview__user=user).all()
        return MyVideoHistorySerializer(_queryset, many=True).data

    def get_watch_marks(self, user):
        """Get user's watch mark histories"""
        _queryset = Video.objects.prefetch_related("watchingmark_set__user").filter(watchingmark__user=user).all()
        return MyVideoHistorySerializer(_queryset, many=True).data

    def get_wishes(self, user):
        """Get user's wish histories"""
        _queryset = Video.objects.prefetch_related("wish_set__user").filter(wish__user=user).all()
        return MyVideoHistorySerializer(_queryset, many=True).data

    def get_stars(self, user):
        """Get user's star histories"""
        _queryset = Video.objects.prefetch_related("starrating_set__user").filter(starrating__user=user).all()
        return MyVideoHistorySerializer(_queryset, many=True).data


class MyVideoHistorySerializer(serializers.ModelSerializer):
    """Video summary histories in Mypage"""

    poster_url = serializers.URLField(source="poster_key", required=False)

    class Meta:
        """Metadata for video histories summary"""

        model = Video
        fields = ["id", "tmdb_id", "poster_url"]

        read_only_fields = ["__all__"]
