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


class GruopPaymentSerializer(serializers.Serializer):
    """Group Payment Serializer"""
    
    payment_id = serializers.IntegerField()# 결제 ID
    amount= serializers.IntegerField()
    request_date_time= serializers.DateField()