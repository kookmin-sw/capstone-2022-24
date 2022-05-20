"""Serializers of groups application for json parsing"""
from group_accounts.serializers import GroupAccountSerializer
from groups.models import Group
from providers.serializers import ProviderSerializer
from rest_framework import serializers


class GroupSerializer(serializers.ModelSerializer):
    """Group model serializer"""

    provider = serializers.SerializerMethodField()
    group_account = serializers.SerializerMethodField()

    class Meta:
        """Metadata of GroupSerializer"""

        model = Group
        fields = "__all__"
        read_only_fields = "__all__"

    def get_provider(self, obj):
        """Get provider data using ProviderSerializer"""
        return ProviderSerializer(obj.provider).data

    def get_group_account(self, obj):
        """Get group account data using GroupAccountSerializer"""
        return GroupAccountSerializer(obj.group_account).data


class GroupPaymentResponseSerializer(serializers.Serializer):
    """Group Serializer for View Response"""

    payment_id = serializers.IntegerField()
    amount = serializers.IntegerField()
    request_date_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        """Meta data for Group Payments Response serializer"""

        read_only_fields = "__all__"

    def create(self, validated_data):
        """method: to not Use"""
        return 0

    def update(self, instance, validated_data):
        """method : to not Use"""
        return 0
