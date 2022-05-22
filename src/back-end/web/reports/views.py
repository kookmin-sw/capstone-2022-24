"""APIs of reports application"""

from math import ceil

from config.exceptions.input import BadFormatException
from django.db.models import Q
from django.utils import timezone
from drf_spectacular.utils import (
    OpenApiExample,
    OpenApiParameter,
    OpenApiResponse,
    extend_schema,
    inline_serializer,
)
from fellows.models import Fellow
from fellows.serializers import FellowReportSerializer, LeaderReportSerializer
from groups.models import Group
from reports.exceptions import (
    AlreadyReportExceptions,
    LeaderExceptions,
    WrongFellowExceptions,
    WrongGroupStateExcetpions,
)
from rest_framework import serializers, status, viewsets
from rest_framework.response import Response


class ReportClass(viewsets.ViewSet):
    """Report Class"""

    @extend_schema(
        tags=["Priority-2", "Video"],
        operation_id="30일이내 내려가는 작품 목록",
        parameters=[
            OpenApiParameter(name="limit", description="number of Videos to display", type=int),
            OpenApiParameter(name="offset", description="number of Videos list Start point", type=int),
        ],
        responses={
            200: OpenApiResponse(
                response=inline_serializer(
                    # meaningless serializer. Just Use to make the example visible
                    name="videoListSerializer",
                    fields={"result": serializers.CharField()},
                ),
                description="작품 목록 제공 성공",
                examples=[OpenApiExample(response_only=True, name="Success Example", value={})],
            )
        },
    )
    def report_group(self, request, group_id):
        """method: Report Group by"""
        _user = request.user
        try:
            _group = Group.objects.get(Q(id=group_id))
            _fellow = Fellow.objects.get(Q(user=_user.id) & Q(group=group_id))
        except Group.DoesNotExist as e:
            raise BadFormatException from e
        except Fellow.DoesNotExist as e:
            raise WrongFellowExceptions from e

        group_status = _group.get_status()

        if group_status in ("Recruited", "Recruiting"):
            raise WrongGroupStateExcetpions
        if _fellow.has_reported:
            raise AlreadyReportExceptions

        report_serializer = FellowReportSerializer(
            _fellow, data={"has_reported": True, "last_modification_date_time": timezone.now()}
        )
        if report_serializer.is_valid(raise_exception=True):
            report_serializer.save()

        fellow_list = Fellow.objects.filter(Q(group=group_id) & Q(has_reported=True))

        report_count = fellow_list.count()
        requeried_report_count = ceil(_group.fellow_set.count() / 2)

        context = {"user_nickname": _user.nickname, "report_count": report_count}

        if report_count >= requeried_report_count:
            # 여기서 폭파 처리 들어감
            context["deleted_group"] = True
        else:
            context["deleted_group"] = False

        return Response(context, status=status.HTTP_201_CREATED)

    def report_leader(self, request, group_id):
        """method: Report leader by fellows"""
        _user = request.user
        try:
            _group = Group.objects.get(Q(id=group_id))
            _fellow = Fellow.objects.get(Q(user=_user.id) & Q(group=group_id))
        except Group.DoesNotExist as e:
            raise BadFormatException from e
        except Fellow.DoesNotExist as e:
            raise WrongFellowExceptions from e

        group_status = _group.get_status()

        if group_status in ("Recruited", "Recruiting"):
            raise WrongGroupStateExcetpions
        if not _fellow.member:
            raise LeaderExceptions
        if _fellow.member.has_reported_leader:
            raise AlreadyReportExceptions

        report_serializer = LeaderReportSerializer(_fellow.member, data={"has_reported_leader": True})
        if report_serializer.is_valid(raise_exception=True):
            report_serializer.save()

        member_list = Fellow.objects.filter(Q(group=group_id) & Q(member__has_reported_leader=True))

        report_count = member_list.count()
        requeried_report_count = ceil(_group.fellow_set.count() / 2)

        context = {"user_nickname": _user.nickname, "report_count": report_count}

        if report_count >= requeried_report_count:
            # 여기서 폭파 처리 들어감
            context["deleted_group"] = True
        else:
            context["deleted_group"] = False

        return Response(context, status=status.HTTP_201_CREATED)

    def destory_group_by_report(self, group_id, request):
        """모임 폭파 로직"""

        return 0

    def exchage_mileage(self, group_id, request):
        """모임 환급 로직"""

        return 0
