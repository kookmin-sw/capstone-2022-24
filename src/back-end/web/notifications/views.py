"""APIs of notifications application"""
from rest_framework.generics import ListAPIView


class NotificationListAndUpdateView(ListAPIView):
    """Notification whole list or read update view"""

    # serializer_class =
    # queryset = No
