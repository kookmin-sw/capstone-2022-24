from .models import BaseApply
from rest_framework import serializers
from users.serializers import UserSerializer
from payments.serializers import PaymentSerializer
from providers.serializers import ProviderSerializer


class BaseApplySerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    payment = serializers.SerializerMethodField()
    provider = serializers.SerializerMethodField()

    class Meta:
        model = BaseApply
        fields = '__all__'

    def get_user(self, obj):
        return UserSerializer(obj.user).data

    def get_payment(self, obj):
        return PaymentSerializer(obj.payment).data

    def get_provider(self, obj):
        return ProviderSerializer(obj.provider).data
