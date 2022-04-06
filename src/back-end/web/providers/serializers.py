from djongo import models

from .models import Provider, Charge, SubscriptionType
from rest_framework import serializers


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = '__all__'


class SubscriptionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionType
        fields = '__all__'


class ChargeSerializer(serializers.ModelSerializer):
    provider = serializers.SerializerMethodField()
    subscriptionType = serializers.SerializerMethodField()

    class Meta:
        model = Charge
        fields = '__all__'

    def get_provider(self, obj):
        return ProviderSerializer(obj.provider).data

    def get_subscription_type(self, obj):
        return SubscriptionTypeSerializer(obj.subscriptionType).data
