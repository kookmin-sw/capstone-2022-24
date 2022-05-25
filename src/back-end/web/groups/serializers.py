"""Serializers of groups application for json parsing"""
from drf_spectacular.utils import extend_schema_serializer
from fellows.serializers import FellowProfileSerializer
from group_accounts.serializers import GroupAccountSerializer
from groups.models import Group
from groups.schemas import GROUP_DETAIL_SERIALIZER_EXAMPLES
from providers.serializers import ProviderSerializer
from reports.serializers import ReportSerializer
from rest_framework import serializers


class GroupPaymentResponseSerializer(serializers.Serializer):
    """Group Serializer for View Response"""

    payment_id = serializers.IntegerField()
    amount = serializers.IntegerField()
    request_date_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        """Meta data for Group Payments Response serializer"""

        read_only_fields = "__all__"

    def create(self, validated_data):
        """method: to not Use"""
        return 0

    def update(self, instance, validated_data):
        """method : to not Use"""
        return 0


@extend_schema_serializer(examples=GROUP_DETAIL_SERIALIZER_EXAMPLES)
class GroupDetailSerializer(serializers.ModelSerializer):
    """Group detail serializer"""

    provider = serializers.SerializerMethodField()
    status = serializers.CharField(source="get_status")
    account = serializers.SerializerMethodField()
    time_stamps = serializers.SerializerMethodField()

    class Meta:
        """Metadata for GroupDetailSerializer"""

        model = Group
        fields = [
            "id",
            "provider",
            "status",
            "account",
            "time_stamps",
        ]
        read_only_fields = ["__all__"]

    def get_provider(self, obj):
        """Get provider in group"""
        return ProviderSerializer(obj.provider).data

    def get_account(self, obj):
        """Get group account that leader registered"""
        return GroupAccountSerializer(obj.group_account).data

    def get_fellows_and_report_with_role(self, obj):
        """Get fellows and reports"""
        _user = self.context.get("request").user
        _fellow_queryset = obj.fellow_set.all()
        _role = None  # front-end request
        _report_meta = dict(reported=False, report_count=0, leader_report_count=0)
        _fellow_users = []
        for f in _fellow_queryset:
            _member = getattr(f, "member", None)
            if _member:
                _report_meta["leader_report_count"] += _member.has_reported_leader
            if f.id == _user.id:
                _report_meta["reported"] = f.has_reported
            _report_meta["report_count"] += f.has_reported
            _fellow_users.append(
                FellowProfileSerializer(
                    f.user, context={"is_leader": not _member, "request": self.context["request"]}
                ).data
            )
            # if this fellow.user is same as login user
            if f.user == _user:
                _role = "모임장" if not _member else "모임원"
        _report = ReportSerializer(_report_meta).data
        return {"fellows": _fellow_users, "report": _report, "role": _role}

    def get_time_stamps(self, obj):
        """Get date time related fields"""
        return GroupTimeStampSerializer(obj).data

    def to_representation(self, instance):
        _representation = super().to_representation(instance)
        _fellows_and_report = self.get_fellows_and_report_with_role(instance)
        _representation.update(_fellows_and_report)
        return _representation


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
