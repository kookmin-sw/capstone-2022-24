"""Common mixins"""
from config.exceptions.result import ResultNotFoundException
from django.http import Http404
from rest_framework.generics import get_object_or_404


class MultipleFieldLookupMixin:
    """Custom mixin to look up by multiple fields"""

    def get_object(self):
        """override get_object method to find by multiple fields"""
        try:
            queryset = self.get_queryset()
            queryset = self.filter_queryset(queryset)
            filters = {}
            for field in self.lookup_fields:
                if field == "user_id":
                    filters[field] = self.request.user.id
                if self.kwargs.get(field, None):
                    filters[field] = self.kwargs[field]
            obj = get_object_or_404(queryset, **filters)  # Lookup the object
            self.check_object_permissions(self.request, obj)
            return obj
        except Http404 as not_found:
            raise ResultNotFoundException() from not_found
