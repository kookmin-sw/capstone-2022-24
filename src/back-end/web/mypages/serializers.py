"""Mypage serializers for json parsing"""
from group_accounts.serializers import GroupAccountSerializer
from groups.models import Group
from groups.serializers import GroupTimeStampSerializer
from providers.serializers import ProviderSerializer
from reports.serializers import ReportSerializer
from rest_framework import serializers
from users.models import User
from users.serializers import UserSerializer
from videos.serializers import MyVideoTotalHistorySerializer


class MyPageSerializer(serializers.Serializer):
    """Mypage serializer including user, wishes, recent-views, star-ratings, watching-marks information"""

    profile = serializers.SerializerMethodField()
    groups = serializers.SerializerMethodField()
    videos = serializers.SerializerMethodField()

    def update(self, instance, validated_data):
        """Do nothing because mypage is read-only"""

    def create(self, validated_data):
        """Do nothing because mypage is read-only"""

    def get_profile(self, user):
        """Get user details of mypage owner"""
        return UserSerializer(user).data

    def get_groups(self, user: User):
        """Get groups details of mypage owner"""
        groups = {}
        _groups = [fellow.group for fellow in user.fellow_set.all()]
        if _groups:
            _default = _groups[0]  # type: Group
            groups["others"] = [ProviderSerializer(g.provider).data for g in _groups[1:]]
            _default_report = dict(
                has_reported=False,
                report_count=0,
                report_leader_count=0,
            )
            groups["default"] = dict(
                provider=ProviderSerializer(_default.provider).data,
                status=_default.status,
                time_stamps=GroupTimeStampSerializer(_default).data,
                fellows=[UserSerializer(u).data for u in User.objects.filter(fellow__group_id=_default.id).all()],
                account=GroupAccountSerializer(_default.group_account).data,
                report=ReportSerializer(_default_report).data,
            )

        # .aggregate(report_leader_count=Count("member__has_reported_leader"), report_count=Count("has_reported"))
        return groups

    def get_videos(self, user):
        """Get videos list that user checked"""
        return MyVideoTotalHistorySerializer(user).data
