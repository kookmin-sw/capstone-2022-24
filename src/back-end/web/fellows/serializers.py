from rest_framework import serializers
from .models import Fellow, Member, Leader
from users.serializers import UserSerializer
from groups.serializers import GroupSerializer
from payments.serializers import PaymentSerializer


class FellowSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    group = serializers.SerializerMethodField()
    payment = serializers.SerializerMethodField()

    class Meta:
        model = Fellow
        fields = '__all__'

    def get_user(self, obj):
        return UserSerializer(obj.user).data

    def get_group(self, obj):
        return GroupSerializer(obj.group).data

    def get_payment(self, obj):
        return PaymentSerializer(obj.payment).data


class MemberSerializer(serializers.ModelSerializer):
    fellow = serializers.SerializerMethodField()

    class Meta:
        model = Member
        fields = '__all__'

    def get_fellow(self, obj):
        return FellowSerializer(obj.provider).data


class LeaderSerializer(serializers.ModelSerializer):
    fellow = serializers.SerializerMethodField()

    class Meta:
        model = Leader
        fields = '__all__'

    def get_fellow(self, obj):
        return FellowSerializer(obj.provider).data
