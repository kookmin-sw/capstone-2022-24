"""Serializers of wish application for json parsing"""
from rest_framework import serializers
from wishes.models import Wish


class WishSerializer(serializers.ModelSerializer):
    """Serializer of Wish model"""

    id = serializers.IntegerField(source="video.id")
    tmdb_id = serializers.IntegerField(source="video.tmdb_id")
    title = serializers.CharField(max_length=200, source="video.title")
    poster_url = serializers.URLField(source="video.poster_key", allow_null=True)

    class Meta:
        """Metadata of Wish serializer"""

        model = Wish
        fields = [
            "id",
            "tmdb_id",
            "title",
            "poster_url",
            "date_time",
        ]
