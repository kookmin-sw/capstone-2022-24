from rest_framework import serializers

from .models import payments


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = payments
        fields = '__all__'
        read_only_fields = '__all__'
