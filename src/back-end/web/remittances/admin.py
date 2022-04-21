"""Admin settings of remittances application"""
from django.contrib import admin
from remittances.models import Remittance, RemittanceReason

admin.site.register(Remittance)
admin.site.register(RemittanceReason)
