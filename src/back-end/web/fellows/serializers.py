"""Serializers of fellows application for json parsing"""
from fellows.models import Fellow, Member
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


class FellowReportSerializer(serializers.ModelSerializer):
    """fellow serializer for group report"""

    class Meta:
        """Metadata of FellowReportSerializer"""

        model = Fellow
        fields = ["has_reported", "last_modification_date_time"]


class MemberReportSerializer(serializers.ModelSerializer):
    """Member serializer for Leader report"""

    class Meta:
        """Metadata of MemberReportSerializer"""

        model = Member
        fields = ["has_reported_leader"]
