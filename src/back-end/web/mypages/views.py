"""APIs of mypages application"""
from drf_spectacular.utils import extend_schema
from mypages.serializers import MyPageSerializer
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import User
from users.serializers import UserSerializer


@extend_schema(tags=["Priority-1", "User"], operation_id="사용자 상세 정보(마이페이지) 조회")
class MyPageDetailView(APIView):
    """User information details

    사용자 정보 조회 (사용자/참여중인 모임/최근 조회작/관람작/찜작 - 첫페이지 작품까지 포함)
    """

    user_queryset = User.objects.all()
    serializer_class = MyPageSerializer

    def get_user(self):
        """Get request user"""
        # get login user
        obj = get_object_or_404(self.user_queryset, id=self.request.user.id)
        # raise permission error if user is invalid
        self.check_object_permissions(self.request, obj)
        return obj

    def get(self, request, *args, **kwargs):
        """GET /users/mypage/"""
        user = self.get_user()
        # serializer = self.serializer_class(user)

        # get mypage data
        profile = UserSerializer(user).data
        groups = {
            "default": {
                "provider": {},
                "status": None,
                "time_stamps": None,
                "report": {
                    "reported": None,
                    "report_count": None,
                    "leader_report_count": None,
                },
                "account": None,
                "fellows": [{"id": None}],
            },
            "others": [
                {"provider": {"id": None, "nickname": None, "link": None, "logo_url": None}},
            ],
        }
        videos = {
            "recent_views": {
                "results": [{"id": None, "tmdb_id": None, "poster_url": None}],
                "page": {
                    "total_page": None,
                    "total_result": None,
                },
            },
            "watch_marks": {
                "results": [{"id": None, "tmdb_id": None, "poster_url": None}],
                "page": {
                    "total_page": None,
                    "total_result": None,
                },
            },
            "wishes": {
                "results": [],
                "page": {
                    "total_page": None,
                    "total_result": None,
                },
            },
            "stars": {
                "results": [],
                "page": {
                    "total_page": None,
                    "total_result": None,
                },
            },
        }
        return Response(data={"profile": profile, "groups": groups, "videos": videos})
