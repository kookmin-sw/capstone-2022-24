from rest_framework import serializers
from .models import Group
from providers.serializers import ProviderSerializer
from group_accounts.serializers import GroupAccountSerializer


class GroupSerializer(serializers.ModelSerializer):
    provider = serializers.SerializerMethodField()
    group_account = serializers.SerializerMethodField()

    class Meta:
        model = Group
        fields = '__all__'
        read_only_fields = '__all__'

    def get_provider(self, obj):
        return ProviderSerializer(obj.provider).data

    def get_group_account(self, obj):
        return GroupAccountSerializer(obj.group_account).data
