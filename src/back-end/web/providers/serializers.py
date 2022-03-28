from .models import providers, charges, subscription_types
from rest_framework import serializers


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = providers
        fields = '__all__'


class SubscriptionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = subscription_types
        fields = '__all__'


class ChargeSerializer(serializers.ModelSerializer):
    provider = serializers.SerializerMethodField()
    subscriptionType = serializers.SerializerMethodField()

    class Meta:
        model = charges
        fields = '__all__'
        read_only_fields = [
            'provider'
        ]

    def get_provider(self, obj):
        return ProviderSerializer(obj.provider).data

    def get_subscription_type(self, obj):
        return SubscriptionTypeSerializer(obj.subscriptionType).data
