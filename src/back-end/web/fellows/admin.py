"""Admin settings of fellow application"""
from django.contrib import admin
from fellows.models import Fellow, Leader, Member

admin.site.register(Fellow)
admin.site.register(Member)
admin.site.register(Leader)
