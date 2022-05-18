"""Serializers of payments application for json parsing"""
from payments.models import Payment
from rest_framework import serializers


class PaymentSerializer(serializers.ModelSerializer):
    """Payment model serializer of json parsing"""

    class Meta:
        """Metadata of PaymentSerializer"""

        model = Payment
        fields = "__all__"
        read_only_fields = "__all__"


class PaymentSaveSerializer(serializers.ModelSerializer):
    """Payment model serializer of saving payments"""

    class Meta:
        """Metadata of PaymentSaveSerializer"""

        model = Payment
        fields = "__all__"
