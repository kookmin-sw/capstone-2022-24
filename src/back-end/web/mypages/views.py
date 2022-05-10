"""APIs of mypages application"""
from drf_spectacular.utils import extend_schema
from rest_framework.generics import RetrieveAPIView, get_object_or_404


@extend_schema(tags=["Priority-1", "User"], operation_id="사용자 상세 정보(마이페이지) 조회")
class MyPageDetailView(RetrieveAPIView):
    """User information details

    사용자 정보 조회 (사용자/참여중인 모임/최근 조회작/관람작/찜작 - 첫페이지 작품까지 포함)
    """

    def get_object(self):
        """Get request user"""
        # get login user
        obj = get_object_or_404(self.get_queryset(), id=self.request.user.id)
        # raise permission error if user is invalid
        self.check_object_permissions(self.request, obj)
        return obj
