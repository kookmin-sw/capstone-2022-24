"""URLs of reports application"""
from django.urls import path
from reports.views import ReportClass

urlpatterns = [
    path("group/", ReportClass.as_view({"post": "report_group"}), name="report group"),
    path("leader/", ReportClass.as_view({"post": "report_leader"}), name="report leader"),
]
