"""Mypage serializers for json parsing"""
from applies.serializers import BaseApplySerializer
from group_accounts.serializers import GroupAccountSerializer
from groups.models import Group
from providers.serializers import ProviderSerializer
from reports.serializers import ReportSerializer
from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from users.models import User
from users.serializers import UserSerializer
from videos.models import Video
from videos.serializers import VideoHistorySerializer


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
        return MyPageGroupSerializer(user).data

    def get_videos(self, user):
        """Get videos list that user checked"""
        return VideoTotalHistorySerializer(user).data


class MyPageGroupSerializer(serializers.Serializer):
    """Group serailizer in mypage format"""

    def update(self, instance, validated_data):
        """Not used"""

    def create(self, validated_data):
        """Not used"""

    def to_representation(self, instance):
        _default = None

        # 1. get group applies
        _member_applies = instance.memberapply_set.all()
        _leader_applies = instance.leaderapply_set.all()

        # 1-1. fill default if user instance is applying leader
        if _leader_applies:
            # get apply details(provider & apply_date_time) and insert status <Recruiting>
            _default = BaseApplySerializer(_leader_applies.first()).data
            _leader_applies = _leader_applies[1:]

        # 1-2. fill default if user instance is applying member
        if not _default and _member_applies:
            _default = BaseApplySerializer(_member_applies.first()).data
            _member_applies = _member_applies[1:]

        _others = [
            BaseApplySerializer(_leader_applies, many=True).data + BaseApplySerializer(_member_applies, many=True).data
        ]

        # 2. get joined groups
        groups = {}
        _joined_groups = [fellow.group for fellow in instance.fellow_set.all()]
        # 2-1. user instance joined groups at least one
        if _joined_groups:
            _others_start_idx = 0
            # _default is not set: user instance is not applying any group
            if not _default:
                _default_group = _joined_groups[0]  # type: Group
                _others_start_idx = 1
                # get report details
                _has_reported = False
                _reported_logs = [
                    (
                        _has_reported := fellow.has_reported if fellow.id == instance.id else fellow.has_reported,
                        fellow.member.has_reported_leader,
                    )
                    for fellow in _default_group.fellow_set
                ]
                _report = list(zip(*_reported_logs))
                _default_report = dict(
                    has_reported=_has_reported, report_count=sum(_report[0]), report_leader_count=sum(_report[1])
                )
                # make _default result
                _default = dict(
                    provider=ProviderSerializer(_default_group.provider).data,
                    status=_default_group.status,
                    time_stamps=MyPageGroupTimeStampSerializer(_default_group).data,
                    fellows=[
                        UserFellowProfileSerializer(u).data
                        for u in User.objects.filter(fellow__group_id=_default_group.id).all()
                    ],
                    account=GroupAccountSerializer(_default_group.group_account).data,
                    report=ReportSerializer(_default_report).data,
                )
            _others += MyPageGroupOthersSerializer(_joined_groups[_others_start_idx:], many=True).data
        groups["default"] = _default
        groups["others"] = _others
        return groups


class MyPageGroupOthersSerializer(serializers.ModelSerializer):
    """Others group serializer in mypage format"""

    provider = serializers.SerializerMethodField()

    class Meta:
        """Metadata of others in mypage groups"""

        model = Group
        fields = ["id", "provider", "status"]
        read_only_fields = ["__all__"]

    def get_provider(self, group):
        """Get provider of one of others' group"""
        return ProviderSerializer(group.provider).data


class MyPageGroupTimeStampSerializer(serializers.ModelSerializer):
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


class UserFellowProfileSerializer(serializers.ModelSerializer):
    """Users' profile in group details"""

    is_leader = serializers.SerializerMethodField()
    is_myself = serializers.SerializerMethodField()

    class Meta:
        """Metadata of UserGroupProfileSerializer"""

        model = User
        fields = ["id", "nickname", "profile_image_url"]

    def get_is_leader(self, user):
        """is user leader in the group?"""
        return bool(user.is_leader)

    def get_is_myself(self, user):
        """is group fellow == me?"""
        return user == CurrentUserDefault()


class VideoTotalHistorySerializer(serializers.Serializer):
    """Mypage total video summary of user's histories"""

    def update(self, instance, validated_data):
        """Not used"""

    def create(self, validated_data):
        """Not usedd"""

    recent_views = serializers.SerializerMethodField(read_only=True)
    watch_marks = serializers.SerializerMethodField(read_only=True)
    wishes = serializers.SerializerMethodField(read_only=True)
    stars = serializers.SerializerMethodField(read_only=True)

    def get_recent_views(self, user):
        """Get user's recent view histories"""
        _queryset = Video.objects.prefetch_related("recentview_set__user").filter(recentview__user=user).all()
        return VideoHistorySerializer(_queryset, many=True).data

    def get_watch_marks(self, user):
        """Get user's watch mark histories"""
        _queryset = Video.objects.prefetch_related("watchingmark_set__user").filter(watchingmark__user=user).all()
        return VideoHistorySerializer(_queryset, many=True).data

    def get_wishes(self, user):
        """Get user's wish histories"""
        _queryset = Video.objects.prefetch_related("wish_set__user").filter(wish__user=user).all()
        return VideoHistorySerializer(_queryset, many=True).data

    def get_stars(self, user):
        """Get user's star histories"""
        _queryset = Video.objects.prefetch_related("starrating_set__user").filter(starrating__user=user).all()
        return VideoHistorySerializer(_queryset, many=True).data
