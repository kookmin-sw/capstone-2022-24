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


class GroupAccountIDSerializer:
    """Serializer of group account identieir"""

    class Meta:
        """Metadata of GroupAccountIDSerializer"""

        model = GroupAccount
        fields = ["identifier"]


class GroupAccountPWSerializer:
    """Serializer of group account password"""

    class Meta:
        """Metadata of GroupAccountPWSerializer"""

        model = GroupAccount
        fields = ["password"]
