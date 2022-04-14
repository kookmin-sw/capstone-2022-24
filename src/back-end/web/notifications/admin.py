"""Admin settings of notificaion application"""
from django.contrib import admin
from notifications.models import Notification, NotificationContent

admin.site.register(Notification)
admin.site.register(NotificationContent)
