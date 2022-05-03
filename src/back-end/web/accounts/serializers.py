"""Serializers of accounts application used to parse into json type"""
from accounts.models import Account, Bank
from rest_framework import serializers


class BankSerializer(serializers.ModelSerializer):
    """Bank model serializer of accounts application"""

    class Meta:
        """Metadata of BankSerializer class"""

        model = Bank
        fields = "__all__"
        extra_kwargs = {"code": {"read_only": True}, "name": {"read_only": True}}


class AccountSerializer(serializers.ModelSerializer):
    """Account model serializer of accounts application"""

    bank = serializers.SerializerMethodField()

    class Meta:
        """Metadata of Accountserializer"""

        model = Account
        fields = "__all__"

    def get_bank(self, obj):
        """Get bank data using BankSerializer"""
        return BankSerializer(obj.bank).data
