"""Admin configurations of providers application"""
from django.contrib import admin
from providers.models import Charge, Provider, SubscriptionType

admin.site.register(Provider)
admin.site.register(Charge)
admin.site.register(SubscriptionType)
