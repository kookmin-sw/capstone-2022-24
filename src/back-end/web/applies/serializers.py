"""Serializers of applies application for json parsing"""
from providers.serializers import ProviderSerializer
from rest_framework import serializers


class BaseApplySerializer(serializers.Serializer):
    """Abstract apply model serializer"""

    def update(self, instance, validated_data):
        """Not used"""

    def create(self, validated_data):
        """Not used"""

    provider = serializers.SerializerMethodField()
    apply_date_time = serializers.DateTimeField()
    status = serializers.SerializerMethodField()

    def get_provider(self, obj):
        """Get provider data using ProviderSerializer"""
        return ProviderSerializer(obj.provider).data

    def get_status(self, obj):
        """Get default group status - <Recruiting>"""
        return "Recruiting"
