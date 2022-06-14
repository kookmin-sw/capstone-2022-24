"""Serializers of providers application for json parsing"""
from drf_spectacular.utils import extend_schema_serializer
from providers.models import Charge, Provider, SubscriptionType
from providers.schemas import PROVIDER_LIST_EXAMPLES
from rest_framework import serializers


class ProviderSerializer(serializers.ModelSerializer):
    """provider model serializer in providers application"""

    name = serializers.CharField(source="get_name_display")
    logo_url = serializers.URLField(source="logo_key")

    class Meta:
        """Meatadata for ProviderSerializer"""

        model = Provider
        fields = ["id", "tmdb_id", "name", "link", "logo_url"]
        read_only_fields = ["__all__"]


class ProviderSummarySerializer(serializers.ModelSerializer):
    """Provider summary"""

    name = serializers.CharField(source="get_name_display")
    logo_url = serializers.URLField(source="logo_key")

    class Meta:
        """Meatadata for ProviderSerializer"""

        model = Provider
        fields = ["id", "name", "logo_url"]
        read_only_fields = ("__all__",)


class ProviderWithChargeSerializer(serializers.ModelSerializer):
    """Provider with charge information"""

    name = serializers.CharField(source="get_name_display")
    charge = serializers.SerializerMethodField()

    class Meta:
        """Metadata for provider"""

        model = Provider
        fields = ["id", "name", "logo_url", "link", "charge"]
        read_only_fields = ["__all__"]

    def get_charge(self, provider):
        """Get member & leader's charge information"""
        if hasattr(provider, "charge") and provider.charge:
            return ChargeSerializer(provider.charge).data
        return None


@extend_schema_serializer(
    examples=PROVIDER_LIST_EXAMPLES,
)
class ProviderListByApplyTypeSerializer(serializers.Serializer):
    """Providers by apply"""

    applied_providers = serializers.SerializerMethodField()
    not_applied_providers = serializers.SerializerMethodField()
    not_supported_providers = serializers.SerializerMethodField()

    def get_applied_providers(self, providers_obj):
        """Get providers by apply type"""
        _applied = providers_obj.get("applied_providers")
        return ProviderWithChargeSerializer(_applied, many=True).data

    def get_not_applied_providers(self, providers_obj):
        """Get providers by apply type"""
        _not_applied = providers_obj.get("not_applied_providers")
        return ProviderWithChargeSerializer(_not_applied, many=True).data

    def get_not_supported_providers(self, providers_obj):
        """Get providers that user can not apply"""
        _not_supported = providers_obj.get("not_supported_providers")
        return ProviderWithChargeSerializer(_not_supported, many=True).data

    def update(self, instance, validated_data):
        """Not used"""

    def create(self, validated_data):
        """Not used"""


class SubscriptionTypeSerializer(serializers.ModelSerializer):
    """SubscriptionType model serializer for json parsing"""

    class Meta:
        """Metadata of SubscriptionTypeSerializer"""

        model = SubscriptionType
        exclude = ("id",)


class ChargeSerializer(serializers.ModelSerializer):
    """Charge model serializer in providers application"""

    subscription_type = serializers.SerializerMethodField()

    class Meta:
        """Meatadata for ChargeSerializer"""

        model = Charge
        read_only_fields = ["__all__"]
        exclude = ("id", "provider", "base_date")

    def get_subscription_type(self, obj):
        """Get subscription_type object data"""
        return SubscriptionTypeSerializer(obj.subscription_type).data
