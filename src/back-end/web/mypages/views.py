"""APIs of mypages application"""
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema
from mypages.schemas import MYPAGE_DETAIL_EXAMPLES
from mypages.serializers import MyPageSerializer
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import User


@extend_schema(
    tags=["Priority-1", "User"],
    operation_id="사용자 상세 정보(마이페이지) 조회",
    examples=MYPAGE_DETAIL_EXAMPLES,
    parameters=[
        OpenApiParameter(
            name="videoLimit",
            type=OpenApiTypes.INT,
            location=OpenApiParameter.QUERY,
            description="video size of limit from offset 0",
        ),
    ],
)
class MyPageDetailView(APIView):
    """User information details

    사용자 정보 조회 (사용자/참여중인 모임/최근 조회작/관람작/찜작 - 첫페이지 작품까지 포함)
    """

    queryset = User.objects.prefetch_related(
        "fellow_set",
        "fellow_set__group",
        "fellow_set__group__provider",
        "fellow_set__group__group_account",
        "fellow_set__member",
        "fellow_set__leader",
        "groupapply_set",
        "groupapply_set__provider",
        "wish_set",
        "wish_set__video",
        "watchingmark_set",
        "watchingmark_set__video",
    )
    serializer_class = MyPageSerializer

    def get_user(self):
        """Get request user"""
        # get login user
        obj = get_object_or_404(self.queryset, id=self.request.user.id)
        # raise permission error if user is invalid
        self.check_object_permissions(self.request, obj)
        return obj

    def get(self, request, *args, **kwargs):
        """GET /users/mypage/"""
        user = self.get_user()
        serializer = self.serializer_class(user, context={"request": request})
        return Response(serializer.data)
