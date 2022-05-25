"""Validators used in serializers related in provider field"""
from providers.models import Provider


def is_supported_provider(provider: Provider):
    """Such Provider supports to use group service: Charge table has provider?"""
    return hasattr(provider, "charge") and provider.charge is not None
