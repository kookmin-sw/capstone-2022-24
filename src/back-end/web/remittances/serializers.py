"""Definitions of Serializers about remittances application for json parsing"""
from payments.serializers import PaymentSerializer
from remittances.models import Remittance, RemittanceReason
from rest_framework import serializers
from users.serializers import UserSerializer


class RemittanceReasonSerializer:
    """Serializer of RemittanceReason model"""

    class Meta:
        """Metadata for remittance reason serializer"""

        model = RemittanceReason
        fields = "__all__"
        read_only_fields = "__all__"


class RemittanceSerializer(serializers.ModelSerializer):
    """Serializer of Remittance model"""

    user = serializers.SerializerMethodField()
    reason = serializers.SerializerMethodField()
    payment = serializers.SerializerMethodField()

    class Meta:
        """Metadata for remittance serializer"""

        model = Remittance
        fields = "__all__"
        read_only_fields = "__all__"

    def get_user(self, obj):
        """Get user data using UserSerializer"""
        return UserSerializer(obj.user).data

    def get_reason(self, obj):
        """Get reason data using RemittanceReasonSerializer"""
        return RemittanceReasonSerializer(obj.reason).data

    def get_payment(self, obj):
        """Get Payment data using PaymentSerializer"""
        return PaymentSerializer(obj.payment).data
