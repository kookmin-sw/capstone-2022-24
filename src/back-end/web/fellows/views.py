"""APIs of fellow application"""
from applies.models import GroupApply
from django.db.models import QuerySet
from fellows.exceptions import GroupFellowsCreationException
from fellows.models import Fellow, Leader, Member
from groups.models import Group


def create_fellows_and_map_into_group_by_applies(group: Group, queryset: QuerySet[GroupApply]):
    """Create fellows using apply queryset and map leader or member by each fellow_type"""
    new_fellows = []

    try:
        for apply in queryset:
            # get information with queryset
            _u = queryset.user
            _p = queryset.payment if hasattr(queryset, "payment") else None
            _fellow = Fellow.objects.create(user=_u, group=group, payment=_p)

            # get fellow role by apply object's fellow_type
            _model = Member
            if apply.fellow_type == "L":
                _model = Leader

            # create leader / member object and append
            _fellow_with_type = _model.objects.create(fellow_id=_fellow.id)
            new_fellows.append(_fellow_with_type)
        return new_fellows
    except Exception as e:
        raise GroupFellowsCreationException() from e
