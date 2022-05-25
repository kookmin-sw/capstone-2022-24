"""URLs of reports application"""
from django.urls import path
from reports.views import ReportView

urlpatterns = [
    path("group/", ReportView.as_view({"post": "report_group", "delete": "cancel_report_group"}), name="report group"),
    path(
        "leader/", ReportView.as_view({"post": "report_leader", "delete": "cancel_report_leader"}), name="report leader"
    ),
]
