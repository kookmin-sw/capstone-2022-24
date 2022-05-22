"""Definitions of serializer for mileages application"""
from config.exceptions.input import UnknownRequestException
from django.core.validators import MaxValueValidator, MinValueValidator
from mileages.exceptions import MileageAmountException
from mileages.models import Mileage
from rest_framework import serializers


class MileageSerializer(serializers.ModelSerializer):
    """Mileage Serializer for json parsing"""

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    now_total_mileages = serializers.SerializerMethodField()

    class Meta:
        """Meta data for Mielage serializer"""

        model = Mileage
        fields = ["user", "amount", "renewal_date_time", "now_total_mileages"]
        read_only_fields = ["renewal_date_time", "now_total_mileages"]
        extra_kwargs = {
            "amount": {
                "required": True,
                "validators": [
                    MinValueValidator(-2147483647),
                    MaxValueValidator(2147483647),
                ],
            },
            "now_total_mileages": {"validators": [MinValueValidator(0), MaxValueValidator(2147483647)]},
        }

    def get_now_total_mileages(self, obj):
        """GET login user's total mileage"""
        return obj.user.total_mileages

    def validate_amount(self, amount):
        """validate amount request value"""
        _user = self.context.get("request").user
        if not self.context.get("request"):
            raise UnknownRequestException
        if not isinstance(amount, int):
            raise MileageAmountException
        if not _user.is_updatable_mileages_with(amount):
            raise MileageAmountException
        return amount

    def to_representation(self, instance):
        """Represent data with serializer instance"""
        # exclude not total mileage in getting mileage history
        _representation = super().to_representation(instance)
        if self.context.get("request").method == "GET":
            _representation.pop("now_total_mileages")
        return _representation
