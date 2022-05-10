"""Serializers of groups application for json parsing"""
from group_accounts.serializers import GroupAccountSerializer
from groups.models import Group
from providers.serializers import ProviderSerializer
from rest_framework import serializers


class GroupSerializer(serializers.ModelSerializer):
    """Group model serializer"""

    provider = serializers.SerializerMethodField()
    group_account = serializers.SerializerMethodField()

    class Meta:
        """Metadata of GroupSerializer"""

        model = Group
        fields = "__all__"
        read_only_fields = "__all__"

    def get_provider(self, obj):
        """Get provider data using ProviderSerializer"""
        return ProviderSerializer(obj.provider).data

    def get_group_account(self, obj):
        """Get group account data using GroupAccountSerializer"""
        return GroupAccountSerializer(obj.group_account).data


class GroupTimeStampSerializer(serializers.ModelSerializer):
    """Date time stamps in group serializer"""

    class Meta:
        """Metadata for GroupTimeStampSerializer"""

        model = Group
        fields = [
            "creation_date_time",
            "start_watching_date_time",
            "end_watching_date_time",
            "end_reporting_date_time",
        ]


class MyPageGroupDefaultSerializer(serializers.ModelSerializer):
    """Default group serailizer in mypage format"""

    provider = serializers.SerializerMethodField()
    time_stamps = serializers.SerializerMethodField()
    report = serializers.SerializerMethodField()
    account = serializers.SerializerMethodField()
    fellows = serializers.SerializerMethodField()

    class Meta:
        """Metadata of MyPageGroupDefaultSerializer"""

        model = Group
        fields = [
            "status",
        ]

    def get_provider(self, group):
        """Get provider that group subscribes"""
        return ProviderSerializer(group.provider).data

    def get_time_stamps(self, group):
        """watching / reporting / creation date time details"""
        return GroupTimeStampSerializer(group).data

    def get_report(self, group):
        """Calculate counts fellows reported"""
        # TODO
        return

    def get_account(self, group):
        """Account details(id & pw & timestamps) that group leader registers"""
        return GroupAccountSerializer(group.group_account).data

    def get_fellows(self, group):
        """Get fellows related in the group"""
        # TODO


class MyPageGroupOthersSerializer(serializers.ModelSerializer):
    """Others group serializer in mypage format"""

    provider = serializers.SerializerMethodField()

    class Meta:
        """Metadata of others in mypage groups"""

        model = Group
        read_only_fields = "__all__"

    def get_provider(self, group):
        """Get provider of one of others' group"""
        return ProviderSerializer(group.provider).data


class MyPageGroupSerializer(serializers.ModelSerializer):
    """Group serailizer in mypage format"""

    default = MyPageGroupDefaultSerializer()
    others = MyPageGroupOthersSerializer(many=True, read_only=True)

    class Meta:
        """Metadata of MyPageGroupSerializer"""

        model = Group
        read_only_fields = "__all__"
