"""Disable CSRF Token"""
from django.utils.deprecation import MiddlewareMixin


class DisableCSRF(MiddlewareMixin):
    """CSRF Token Disable middleware"""

    def process_request(self, request):
        """prevent to enforce csrf token checks"""
        setattr(request, "_dont_enforce_csrf_checks", True)
