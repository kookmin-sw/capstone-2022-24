"""Serializers of applies application for json parsing"""
from applies.models import LeaderApply, MemberApply
from payments.serializers import PaymentSerializer
from providers.serializers import ProviderSerializer
from rest_framework import serializers
from users.serializers import UserSerializer


class BaseApplySerializer(serializers.Serializer):
    """Abstract apply model serializer"""

    def update(self, instance, validated_data):
        """Not used"""

    def create(self, validated_data):
        """Not used"""

    fellows = serializers.SerializerMethodField()
    provider = serializers.SerializerMethodField()
    apply_date_time = serializers.DateTimeField()
    status = serializers.SerializerMethodField()

    def get_provider(self, obj):
        """Get provider data using ProviderSerializer"""
        return ProviderSerializer(obj.provider).data

    def get_status(self, obj):
        """Get default group status - <Recruiting>"""
        return "Recruiting"

    def get_fellows(self, obj):
        """Empty fellows because group is not composed yet"""
        return []


class MemberApplySerializer(serializers.ModelSerializer):
    """Member Apply Serializer for MemberApply model"""

    user = serializers.SerializerMethodField()
    payment = serializers.SerializerMethodField()
    provider = serializers.SerializerMethodField()

    class Meta:
        """MetaData for MemberApplySerializer"""

        model = MemberApply
        fields = ("id", "user", "payment", "provider", "apply_date_time")

    def get_user(self, obj):
        """Get user data using UserSerializer"""
        return UserSerializer(obj.user).data

    def get_payment(self, obj):
        """Get payment data using PaymentSerializer"""
        return PaymentSerializer(obj.payment).data

    def get_provider(self, obj):
        """Get provider data using ProviderSerializer"""
        return ProviderSerializer(obj.provider).data


class LeaderApplySerializer(serializers.ModelSerializer):
    """Leader Apply Serializer for LeaderApply model"""

    user = serializers.SerializerMethodField()
    provider = serializers.SerializerMethodField()

    class Meta:
        """MetaData for LeaderApplySerializer"""

        model = LeaderApply
        fields = ("id", "user", "provider", "apply_date_time")

    def get_user(self, obj):
        """Get user data using UserSerializer"""
        return UserSerializer(obj.user).data

    def get_provider(self, obj):
        """Get provider data using ProviderSerializer"""
        return ProviderSerializer(obj.provider).data


class MemberCancelSerializer(serializers.Serializer):
    """Member Cancel Serializer for View Response"""

    user_id = serializers.IntegerField()
    payment_id = serializers.IntegerField()
    provider_id = serializers.IntegerField()

    def update(self, instance, validated_data):
        """Not used"""

    def create(self, validated_data):
        """Not used"""


class LeaderCancelSerializer(serializers.Serializer):
    """Leader Cancel Serializer for View Response"""

    user_id = serializers.IntegerField()
    provider_id = serializers.IntegerField()

    def update(self, instance, validated_data):
        """Not used"""

    def create(self, validated_data):
        """Not used"""
