"""Serializers for json parsing used in reports application"""
from rest_framework import serializers


class ReportSerializer(serializers.Serializer):
    """Report serializer that group leader or fellows submits"""

    def update(self, instance, validated_data):
        """Not used"""

    def create(self, validated_data):
        """Not used"""

    reported_group = serializers.BooleanField(
        read_only=True,
        default=False,
    )
    reported_leader = serializers.BooleanField(
        read_only=True,
        default=False,
    )
    report_count = serializers.IntegerField(
        read_only=True,
        min_value=0,
        # max_value=NUMBER_OF_FELLOWS
    )
    leader_report_count = serializers.IntegerField(
        read_only=True,
        min_value=0,
        # max_value=NUMBER_OF_FELLOWS-1
    )
