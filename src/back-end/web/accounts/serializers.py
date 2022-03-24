from .models import Bank, Account
from rest_framework import serializers


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = '__all__'
        extra_kwargs = {
            'code': {
                'read_only': True
            },
            'name': {
                'read_only': True
            }
        }


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'
