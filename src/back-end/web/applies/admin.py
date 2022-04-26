"""Admin configurations of applies application"""
from applies.models import LeaderApply, MemberApply
from django.contrib import admin

admin.site.register(LeaderApply)
admin.site.register(MemberApply)
