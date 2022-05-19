"""Serializers of providers application for json parsing"""

from providers.models import Charge, Provider, SubscriptionType
from providers.views import get_providers_by_user_apply_type
from rest_framework import serializers


class ProviderSerializer(serializers.ModelSerializer):
    """provider model serializer in providers application"""

    logo_url = serializers.URLField(source="logo_key")

    class Meta:
        """Meatadata for ProviderSerializer"""

        model = Provider
        fields = ["id", "tmdb_id", "name", "link", "logo_url"]
        read_only_fields = ["__all__"]


class ProviderSummarySerializer(serializers.ModelSerializer):
    """Provider summary"""

    class Meta:
        """Metadata for provider"""

        model = Provider
        fields = ["id", "name", "logo_url", "link"]
        read_only_fields = ["__all__"]


class ProviderListByApplyTypeSerializer(serializers.Serializer):
    """Providers by apply"""

    applied_providers = serializers.SerializerMethodField(method_name="get_providers")
    not_applied_providers = serializers.SerializerMethodField(method_name="get_providers")

    def get_providers(self, user):
        """Get providers by apply type"""
        return get_providers_by_user_apply_type(user)

    def update(self, instance, validated_data):
        """Not used"""

    def create(self, validated_data):
        """Not used"""


class SubscriptionTypeSerializer(serializers.ModelSerializer):
    """SubscriptionType model serializer for json parsing"""

    class Meta:
        """Metadata of SubscriptionTypeSerializer"""

        model = SubscriptionType
        fields = "__all__"


class ChargeSerializer(serializers.ModelSerializer):
    """Charge model serializer in providers application"""

    provider = serializers.SerializerMethodField()
    subscriptionType = serializers.SerializerMethodField()

    class Meta:
        """Meatadata for ChargeSerializer"""

        model = Charge
        fields = "__all__"

    def get_provider(self, obj):
        """Get proivder data using ProviderSerializer"""
        return ProviderSerializer(obj.provider).data

    def get_subscription_type(self, obj):
        """Get subscription type data using SubscriptionTypeSerializer"""
        return SubscriptionTypeSerializer(obj.subscription_type).data
