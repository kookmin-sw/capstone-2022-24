from .models import banks, accounts
from rest_framework import serializers


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = banks
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
    bank = BankSerializer(
        many=False,
        read_only=True
    )
    class Meta:
        model = accounts
        fields = (
            '_id',
            'name'
        )
