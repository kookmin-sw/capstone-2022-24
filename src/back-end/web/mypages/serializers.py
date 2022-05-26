"""Mypage serializers for json parsing"""
from applies.serializers import BaseApplySerializer
from groups.models import Group
from groups.serializers import GroupDetailSerializer
from mypages.pagination import VideoHistoryPagination
from providers.serializers import ProviderSerializer
from rest_framework import serializers
from users.models import User
from users.serializers import UserSerializer
from videos.models import Video
from videos.serializers import VideoHistorySerializer
from watching_marks.serializers import WatchingMarkListSerializer
from wishes.serializers import WishListSerializer


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
        return MyPageGroupSerializer(user, context={"request": self.context.get("request")}).data

    def get_videos(self, user):
        """Get videos list that user checked"""
        return VideoTotalHistorySerializer(user, context={"request": self.context.get("request")}).data


class MyPageGroupSerializer(serializers.Serializer):
    """Group serailizer in mypage format"""

    def update(self, instance, validated_data):
        """Not used"""

    def create(self, validated_data):
        """Not used"""

    def to_representation(self, instance):
        _default = None

        # 1-1. get group applies
        _applies = instance.groupapply_set.all()
        _others = []

        # 1-2. fill default if user instance is applying group
        if _applies:
            # get apply details(provider & apply_date_time) and insert status <Recruiting>
            _default = BaseApplySerializer(_applies.first()).data
            _other_applies = _applies[1:]
            if _other_applies:
                _others = BaseApplySerializer(_applies[1:], many=True).data

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
                # get _default group detail
                _default = GroupDetailSerializer(_default_group, context={"request": self.context.get("request")}).data
            _others += MyPageGroupOthersSerializer(_joined_groups[_others_start_idx:], many=True).data
        groups["default"] = _default
        groups["others"] = _others
        return groups


class MyPageGroupOthersSerializer(serializers.ModelSerializer):
    """Others group serializer in mypage format"""

    provider = serializers.SerializerMethodField()
    fellows = serializers.ListField(default=[])

    class Meta:
        """Metadata of others in mypage groups"""

        model = Group
        fields = ["id", "provider", "status", "fellows"]
        read_only_fields = ["__all__"]

    def get_provider(self, group):
        """Get provider of one of others' group"""
        return ProviderSerializer(group.provider).data


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

    def get_paginated_videos(self, queryset, serializer=VideoHistorySerializer):
        """Get paginated video histories"""
        paginator = VideoHistoryPagination()
        _page = paginator.paginate_queryset(queryset, self.context.get("request"))
        return paginator.get_paginated_result(serializer(_page, many=True).data)

    def get_recent_views(self, user):
        """Get user's recent view histories"""
        _queryset = Video.objects.prefetch_related("recentview_set__user").filter(recentview__user=user).all()
        return self.get_paginated_videos(_queryset)

    def get_watch_marks(self, user):
        """Get user's watch mark histories"""
        _watch_marks = user.watchingmark_set.order_by("-date_time").all()
        return self.get_paginated_videos(_watch_marks, WatchingMarkListSerializer)

    def get_wishes(self, user):
        """Get user's wish histories"""
        _wishes = user.wish_set.order_by("-date_time").all()
        return self.get_paginated_videos(_wishes, WishListSerializer)

    def get_stars(self, user):
        """Get user's star histories"""
        _queryset = Video.objects.prefetch_related("starrating_set__user").filter(starrating__user=user).all()
        return self.get_paginated_videos(_queryset)
