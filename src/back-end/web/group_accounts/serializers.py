"""Serializers of group_accounts application for json parsing"""
from group_accounts.models import GroupAccount
from rest_framework import serializers


class GroupAccountSerializer(serializers.ModelSerializer):
    """Serializer of GroupAccount model"""

    class Meta:
        """Metadata of GroupAccountSerializer"""

        model = GroupAccount
        fields = "__all__"
        read_only_fields = ["creationDateTime", "lastModificationDateTime"]
