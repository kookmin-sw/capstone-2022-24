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
    bank = serializers.SerializerMethodField()

    class Meta:
        model = Account
        fields = '__all__'

    def get_bank(self, obj):
        return BankSerializer(obj.bank).data
