"""APIs of providers application"""
from django.db.models import Q
from providers.models import Provider
from users.models import User


def get_providers_by_user_apply_type(login_user: User):
    """Get providers in two categories: applied,joined & not applied"""

    # get providers queryset
    _queryset = Provider.objects.prefetch_related(
        "memberapply_set",
        "memberapply_set__user",
        "leaderapply_set",
        "leaderapply_set__user",
        "group_set",
        "group_set__fellow_set",
        "group_set__fellow_set__user",
    )

    # get applied providers
    _filter = (
        Q(memberapply_set__user=login_user)
        | Q(leaderapply_set__user=login_user)
        | Q(group_set__fellow_set__user=login_user)
    )
    _applied_providers = _queryset.filter(_filter).all()

    # get not-applied providers
    _not_applied_providers = _queryset.difference(_applied_providers).all()

    # make dictionary data
    providers = {
        "applied_providers": _applied_providers,
        "not_applied_providers": _not_applied_providers,
    }
    return providers
