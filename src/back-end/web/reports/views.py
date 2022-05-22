"""APIs of reports application"""

from math import ceil

from django.db.models import Q
from django.utils import timezone
from drf_spectacular.utils import OpenApiResponse, extend_schema, inline_serializer
from fellows.models import Fellow
from fellows.serializers import FellowReportSerializer, LeaderReportSerializer
from groups.models import Group
from reports.exceptions import (
    AlreadyReportExceptions,
    GroupNotFoundExceptions,
    LeaderExceptions,
    NoneReportExceptions,
    WrongFellowExceptions,
    WrongGroupStateExcetpions,
)
from rest_framework import serializers, status, viewsets
from rest_framework.response import Response


class ReportClass(viewsets.ViewSet):
    """Report Class"""

    @extend_schema(
        tags=["Priority-2", "Group"],
        operation_id="모임 신고",
        responses={
            201: OpenApiResponse(
                response=inline_serializer(
                    # meaningless serializer. Just Use to make the example visible
                    name="GroupReportSerializer",
                    fields={
                        "user_nickname": serializers.CharField(),
                        "report_count": serializers.IntegerField(),
                        "deleted_group": serializers.BooleanField(),
                    },
                ),
                description="모임 신고 성공",
                examples=[],
            )
        },
    )
    def report_group(self, request, group_id):
        """method: Report Group by fellows"""
        _user = request.user
        try:
            _group = Group.objects.get(Q(id=group_id))
            _fellow = Fellow.objects.get(Q(user=_user.id) & Q(group=group_id))
        except Group.DoesNotExist as e:
            raise GroupNotFoundExceptions from e
        except Fellow.DoesNotExist as e:
            raise WrongFellowExceptions from e

        group_status = _group.get_status()

        if group_status in ("Recruited", "Recruiting", "Expired"):
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
            _group.delete()
            context["deleted_group"] = True
        else:
            context["deleted_group"] = False

        return Response(context, status=status.HTTP_201_CREATED)

    @extend_schema(
        tags=["Priority-2", "Group"],
        operation_id="모임장 신고",
        responses={
            201: OpenApiResponse(
                response=inline_serializer(
                    # meaningless serializer. Just Use to make the example visible
                    name="GroupReportSerializer",
                    fields={
                        "user_nickname": serializers.CharField(),
                        "report_count": serializers.IntegerField(),
                        "deleted_group": serializers.BooleanField(),
                    },
                ),
                description="모임장 신고 성공",
                examples=[],
            )
        },
    )
    def report_leader(self, request, group_id):
        """method: Report leader by members"""
        _user = request.user
        try:
            _group = Group.objects.get(Q(id=group_id))
            _fellow = Fellow.objects.get(Q(user=_user.id) & Q(group=group_id))
        except Group.DoesNotExist as e:
            raise GroupNotFoundExceptions from e
        except Fellow.DoesNotExist as e:
            raise WrongFellowExceptions from e

        group_status = _group.get_status()

        if group_status in ("Recruited", "Recruiting", "Expired"):
            raise WrongGroupStateExcetpions

        try:
            if _fellow.member.has_reported_leader:
                raise AlreadyReportExceptions
        except Fellow.member.RelatedObjectDoesNotExist as e:
            raise LeaderExceptions from e

        report_serializer = LeaderReportSerializer(_fellow.member, data={"has_reported_leader": True})
        if report_serializer.is_valid(raise_exception=True):
            report_serializer.save()

        member_list = Fellow.objects.filter(Q(group=group_id) & Q(member__has_reported_leader=True))

        report_count = member_list.count()
        requeried_report_count = ceil(_group.fellow_set.count() / 2)

        context = {"user_nickname": _user.nickname, "report_count": report_count}

        if report_count >= requeried_report_count:
            _group.delete()
            context["deleted_group"] = True
        else:
            context["deleted_group"] = False

        return Response(context, status=status.HTTP_201_CREATED)

    @extend_schema(
        tags=["Priority-3", "Group"],
        operation_id="모임 신고 취소",
        responses={
            204: OpenApiResponse(
                description="모임 신고 취소 성공",
            )
        },
    )
    def cancel_report_group(self, request, group_id):
        """method: Report group Cancel"""
        _user = request.user
        try:
            _group = Group.objects.get(Q(id=group_id))
            _fellow = Fellow.objects.get(Q(user=_user.id) & Q(group=group_id))
        except Group.DoesNotExist as e:
            raise GroupNotFoundExceptions from e
        except Fellow.DoesNotExist as e:
            raise WrongFellowExceptions from e

        if not _fellow.has_reported:
            raise NoneReportExceptions

        report_serializer = FellowReportSerializer(
            _fellow, data={"has_reported": False, "last_modification_date_time": timezone.now()}
        )
        if report_serializer.is_valid(raise_exception=True):
            report_serializer.save()

        return Response(status=status.HTTP_204_NO_CONTENT)

    @extend_schema(
        tags=["Priority-3", "Group"],
        operation_id="모임 신고 취소",
        responses={
            204: OpenApiResponse(
                description="모임 신고 취소 성공",
            )
        },
    )
    def cancel_report_leader(self, request, group_id):
        """method: Report leader Cancel"""
        _user = request.user
        try:
            _group = Group.objects.get(Q(id=group_id))
            _fellow = Fellow.objects.get(Q(user=_user.id) & Q(group=group_id))
        except Group.DoesNotExist as e:
            raise GroupNotFoundExceptions from e
        except Fellow.DoesNotExist as e:
            raise WrongFellowExceptions from e

        try:
            if not _fellow.member.has_reported_leader:
                raise NoneReportExceptions
        except Fellow.member.RelatedObjectDoesNotExist as e:
            raise LeaderExceptions from e

        report_serializer = LeaderReportSerializer(_fellow.member, data={"has_reported_leader": False})
        if report_serializer.is_valid(raise_exception=True):
            report_serializer.save()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def destory_group_by_report_group(self, _group, group_status):
        """method that refunds mileage after meeting delete by Report group"""

        if group_status == "Reviewing":  # 검토기간 = 맴버들은 100퍼 환급해줍니다
            """TODO"""
        elif group_status == "Watching":  # 검토기간 지남 = 모임장만 돌려줍니다
            """TODO"""
        else:
            raise WrongGroupStateExcetpions

        return True

    def destory_group_by_report_leader(self, _group, group_status):
        """method that refunds mileage after meeting delete by Report leader"""

        if group_status == "Reviewing":  # 검토기간 = 맴버들은 100퍼 환급해줍니다
            """TODO"""
        elif group_status == "Watching":  # 검토기간 지남 = 모임원만 돌려줍니다
            """TODO"""
        else:
            raise WrongGroupStateExcetpions

        return True
