"""Serializers of applies application for json parsing"""
from applies.models import BaseApply
from payments.serializers import PaymentSerializer
from providers.serializers import ProviderSerializer
from rest_framework import serializers
from users.serializers import UserSerializer


class BaseApplySerializer(serializers.ModelSerializer):
    """Abstract apply model serializer"""

    user = serializers.SerializerMethodField()
    payment = serializers.SerializerMethodField()
    provider = serializers.SerializerMethodField()

    class Meta:
        """Metadata of BaseApplySerializer"""

        model = BaseApply
        fields = "__all__"

    def get_user(self, obj):
        """Get user data using UserSerializer"""
        return UserSerializer(obj.user).data

    def get_payment(self, obj):
        """Get payment data using PaymentSerializer"""
        return PaymentSerializer(obj.payment).data

    def get_provider(self, obj):
        """Get provider data using ProviderSerializer"""
        return ProviderSerializer(obj.provider).data
