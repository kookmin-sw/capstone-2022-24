"""Serializers of wish application for json parsing"""
from rest_framework import serializers
from watching_marks.models import WatchingMark


class WatchingMarkListSerializer(serializers.ModelSerializer):
    """Serializer of WatchingMark model"""

    id = serializers.IntegerField(source="video.id")
    category = serializers.CharField(source="video.category", max_length=2)
    title = serializers.CharField(max_length=200, source="video.title")
    poster_url = serializers.URLField(source="video.poster_key", allow_null=True)
    date = serializers.DateField(source="get_date")
    time = serializers.TimeField(source="get_time")

    class Meta:
        """Metadata of WatchingMark List serializer"""

        model = WatchingMark
        fields = ["id", "category", "title", "poster_url", "date", "time"]
        read_only_fields = ["__all__"]


class WatchingMarkSerializer(serializers.ModelSerializer):
    """WatchingMarkSerializer used in create & destroy view"""

    watching_mark_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        """Metadata of Wish serializer"""

        model = WatchingMark
        fields = ["id", "user", "video", "watching_mark_count", "date_time"]

    def get_watching_mark_count(self, obj):
        """Get modified watch_count"""
        return obj.video.videototalcount.watch_count
