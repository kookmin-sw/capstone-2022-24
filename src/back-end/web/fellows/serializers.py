"""Serializers of fellows application for json parsing"""
from fellows.models import Fellow, Leader, Member
from groups.serializers import GroupSerializer
from payments.serializers import PaymentSerializer
from rest_framework import serializers
from users.serializers import UserSerializer


class FellowSerializer(serializers.ModelSerializer):
    """Serializer of Fellow model"""

    user = serializers.SerializerMethodField()
    group = serializers.SerializerMethodField()
    payment = serializers.SerializerMethodField()

    class Meta:
        """Meta data of FellowSerializer"""

        model = Fellow
        fields = "__all__"

    def get_user(self, obj):
        """Get user data using UserSerializer"""
        return UserSerializer(obj.user).data

    def get_group(self, obj):
        """Get group data using GroupSerializer"""
        return GroupSerializer(obj.group).data

    def get_payment(self, obj):
        """Get payment data using PaymentSerializer"""
        return PaymentSerializer(obj.payment).data


class MemberSerializer(serializers.ModelSerializer):
    """Serializer of Member model"""

    fellow = serializers.SerializerMethodField()

    class Meta:
        """Meta data of MemberSerializer"""

        model = Member
        fields = "__all__"

    def get_fellow(self, obj):
        """Get fellow data using FellowSerializer"""
        return FellowSerializer(obj.provider).data


class LeaderSerializer(serializers.ModelSerializer):
    """Serializer of Leader model"""

    fellow = serializers.SerializerMethodField()

    class Meta:
        """Meta data of LeaderSerializer"""

        model = Leader
        fields = "__all__"

    def get_fellow(self, obj):
        """Get fellow data using FellowSerializer"""
        return FellowSerializer(obj.provider).data
