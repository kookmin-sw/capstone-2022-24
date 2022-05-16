"""groups URL Configuration"""
from django.urls import path
from groups.views import GroupApplyView, GruopPaymentView

urlpatterns = [
    path("payments/", GruopPaymentView.as_view({"post": "payment"}), name="group payments"),
]
'''
path("applies/member/", GroupApplyView.as_view(), name="member apply"),
    # 1. 모임 구성 전이므로 모임 구분 identifier 없음2. 모임원 이용료 결제 > 모임원 신청 API 호출
    path("applies/leader/", GroupApplyView.as_view(), name="leader apply"),
    # 1. 모임 구성 전이므로 모임 구분 identifier 없음. 2. 모임원 이용료 결제 > 모임원 신청 API 호출
    path("applies/member/", GroupApplyView.as_view(), name="member refund"),
    # 모집 중일 때 구성원의 취소 요청 (환불 처리함)
    path("applies/leader/", GroupApplyView.as_view(), name="leader cancel"),
    # 모집 중일 때 구성원의 취소 요청
'''