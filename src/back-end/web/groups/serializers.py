"""Serializers of groups application for json parsing"""
from collections import OrderedDict

from applies.models import LeaderApply, MemberApply
from applies.serializers import BaseApplySerializer
from django.db.models import Count, F, Value
from fellows.models import Fellow
from group_accounts.serializers import GroupAccountSerializer
from groups.models import Group
from providers.serializers import ProviderSerializer
from rest_framework import serializers
from users.serializers import UserGroupProfileSerializer


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

    provider = ProviderSerializer()
    fellows = serializers.SerializerMethodField()
    account = GroupAccountSerializer(source="group_account")
    time_stamps = serializers.SerializerMethodField()
    report = serializers.SerializerMethodField()

    class Meta:
        """Metadata of MyPageGroupDefaultSerializer"""

        model = Group
        fields = ["provider", "account", "status", "fellows", "report", "time_stamps"]

    def get_provider(self, group):
        """Get provider that group subscribes"""
        return ProviderSerializer(group.provider).data

    def get_report(self, group):
        """Calculate counts fellows reported"""
        user_id = self.context.user.id
        # 모임 -> 구성원 조회 - 모임 신고 여부 확인 x 구성원- 카운트
        # 모임 -> 구성원 -> 모임원 조회 - 모임장 신고 여부 확인 x 모임원 - 카운트
        _report = (
            Fellow.objects.select_related("group")
            .filter(group=group)
            .prefetch_related("member")
            .aggregate(report_leader_count=Count("member__has_reported_leader"), report_count=Count("has_reported"))
        )
        has_reported = _report.get(user__id=user_id).has_reported
        report = OrderedDict()
        report["has_reported"] = has_reported
        report["report_count"] = _report["report_count"]
        report["report_leader_count"] = _report["report_leader_count"]
        return report

    def get_fellows(self, group):
        """Get fellows related in the group"""
        mypage_user = self.context["user"]
        # 모임 -> 구성원 목록 조회
        # 구성원 -> 사용자 조회: id, profile_image_url, nickname 필드 얻기
        # 구성원 -> 모임장 조회: isLeader 필드
        # 구성원.user_id == request.user.id: isMyself 필드
        fellows = (
            Fellow.objects.select_related("group")
            .filter(group=group)
            .select_related("user")
            .prefetch_related("leader")
            .annotate(is_leaders=Value("leader__id" == F(id)), is_myself=Value(mypage_user.id == F(id)))
            .all()
        )
        return UserGroupProfileSerializer(fellows)

    def get_time_stamps(self, group):
        """Get time stamps related to creatae/watching time"""
        return GroupTimeStampSerializer(group)


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


class MyPageGroupSerializer(serializers.Serializer):
    """Group serailizer in mypage format"""

    def update(self, instance, validated_data):
        """Not used"""

    def create(self, validated_data):
        """Not used"""

    def to_representation(self, instance):
        # 1. get applies (and each provider")
        # 사용자의 모임 신청 & 모임의 OTT 구하기
        _leader_applies = (
            LeaderApply.objects.prefetch_related("user").filter(user=instance).select_related("provider").all()
        )
        _member_applies = (
            MemberApply.objects.prefetch_related("user").filter(user=instance).select_related("provider").all()
        )
        _default = None

        if _leader_applies.exists():
            _default = BaseApplySerializer(_leader_applies.first()).data
            # get apply details(provider & apply_date_time) and insert status <Recruiting>
            _leader_applies = _leader_applies[1:]

        if not _default and _member_applies.exists():
            _default = BaseApplySerializer(_member_applies.first()).data
            _member_applies = _member_applies[1:]

        _others = (
            BaseApplySerializer(_leader_applies, many=True).data + BaseApplySerializer(_member_applies, many=True).data
        )

        for _other in _others:
            _others.status = "Recruiting"

        # 2. get groups
        _joined_groups = (
            Group.objects.select_related("provider", "group_account")
            .prefetch_related("fellow_set__user")
            .filter(fellow__user_id=instance.id)
        )

        # 2-1. if user group apply does not exists
        # 모임 신청이 하나 이상 있으면
        # 2-1-1. 사용자가 구성원으로 속한 모임 구하기
        # 2-1-2. 모임과 모임별 OTT만 구하면 됨
        if _default:
            _others += list(MyPageGroupOthersSerializer(_joined_groups, many=True, context={"user": instance}).data)

        # 2-2. if user group applies(or apply) exist(s)
        # 모임 신청이 없으면
        else:
            # 사용자가 구성원으로 속한 모임 구하기
            # 모임별 > OTT, 모임 계정, 모임의 구성원, 구성원의 모임원/모임장 구하기
            # 2-2-1. 모임이 있으면
            if _joined_groups:
                # 2-2-1-1. default 설정
                _default = MyPageGroupDefaultSerializer(_joined_groups.first(), context={"user": instance})
                # 2-2-1-1-1. default의 상세 정보 주입
                # 2-2-1-2. others 설정
                _others = list(MyPageGroupOthersSerializer(_joined_groups[1:], many=True).data)

        mypage_groups = OrderedDict()
        mypage_groups["default"] = _default
        mypage_groups["others"] = _others
        return mypage_groups
