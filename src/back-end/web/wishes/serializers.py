"""Serializers of wish application for json parsing"""
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from wishes.models import Wish


class WishListSerializer(serializers.ModelSerializer):
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
        read_only_fields = ["__all__"]


class WishSerializer(serializers.ModelSerializer):
    """WishSerializer used in create & destroy view"""

    class Meta:
        """Metadata of Wish serializer"""

        model = Wish
        fields = "__all__"
        validators = [
            UniqueTogetherValidator(
                queryset=Wish.objects.all(),
                fields=["user", "video"],
            )
        ]
