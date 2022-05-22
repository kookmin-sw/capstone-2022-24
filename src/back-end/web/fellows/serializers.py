"""Serializers of fellows application for json parsing"""
from rest_framework import serializers
from users.models import User


class FellowProfileSerializer(serializers.ModelSerializer):
    """Users' profile in group details"""

    is_leader = serializers.SerializerMethodField()
    is_myself = serializers.SerializerMethodField()

    class Meta:
        """Metadata of UserGroupProfileSerializer"""

        model = User
        fields = ["id", "nickname", "profile_image_url", "is_leader", "is_myself"]

    def get_is_leader(self, user):
        """is user leader in the group?"""
        return self.context.get("is_leader", False)

    def get_is_myself(self, user):
        """is group fellow == me?"""
        return user == self.context.get("request").user
