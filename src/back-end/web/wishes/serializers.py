"""Serializers of wish application for json parsing"""
from drf_spectacular.utils import extend_schema_serializer
from rest_framework import serializers
from wishes.models import Wish
from wishes.schemas import WISH_SERIALIZER_EXAMPLES


class WishListSerializer(serializers.ModelSerializer):
    """Serializer of Wish model"""

    id = serializers.IntegerField(source="video.id")
    category = serializers.CharField(source="video.category", max_length=2)
    title = serializers.CharField(max_length=200, source="video.title")
    poster_url = serializers.URLField(source="video.poster_key", allow_null=True)
    date = serializers.DateField(source="get_date")
    time = serializers.TimeField(source="get_time")

    class Meta:
        """Metadata of Wish serializer"""

        model = Wish
        fields = ["id", "category", "title", "poster_url", "date", "time"]
        read_only_fields = ["__all__"]


@extend_schema_serializer(examples=WISH_SERIALIZER_EXAMPLES)
class WishSerializer(serializers.ModelSerializer):
    """WishSerializer used in create & destroy view"""

    wish_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        """Metadata of Wish serializer"""

        model = Wish
        fields = ["id", "user", "video", "wish_count", "date_time"]

    def get_wish_count(self, obj):
        """Get modified wish_count"""
        return obj.video.videototalcount.wish_count
