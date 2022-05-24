"""Serializers of applies application for json parsing"""
from applies.models import GroupApply
from applies.schemas import GROUP_APPLY_EXAMPLES
from config.exceptions.input import NotSupportedProviderException
from drf_spectacular.utils import extend_schema_serializer
from fellows.serializers import FellowProfileSerializer
from payments.serializers import PaymentSerializer
from providers.exceptions import NotFoundProviderException
from providers.models import Provider
from providers.serializers import ProviderSerializer
from providers.validators import is_supported_provider
from rest_framework import serializers


class BaseApplySerializer(serializers.Serializer):
    """Abstract apply model serializer (used in mypage group section"""

    def update(self, instance, validated_data):
        """Not used"""

    def create(self, validated_data):
        """Not used"""

    fellows = serializers.SerializerMethodField()
    provider = serializers.SerializerMethodField()
    apply_date_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    status = serializers.SerializerMethodField()

    def get_provider(self, obj):
        """Get provider data using ProviderSerializer"""
        return ProviderSerializer(obj.provider).data

    def get_status(self, obj):
        """Get default group status - <Recruiting>"""
        return "Recruiting"

    def get_fellows(self, obj):
        """Empty fellows because group is not composed yet"""
        return []


@extend_schema_serializer(examples=GROUP_APPLY_EXAMPLES)
class GroupApplySerializer(serializers.ModelSerializer):
    """Member Apply Serializer for MemberApply model"""

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    payment = serializers.SerializerMethodField(required=False, allow_null=True)
    provider_id = serializers.IntegerField()

    class Meta:
        """MetaData for MemberApplySerializer"""

        model = GroupApply
        fields = ("user", "payment", "provider_id", "apply_date_time")
        read_only_fields = ["apply_date_time"]

    def get_payment(self, obj):
        """Get payment data using PaymentSerializer"""
        if hasattr(obj, "payment"):
            return PaymentSerializer(obj.payment).data
        return None

    def create(self, validated_data):
        _apply_path = self.context.get("request").get_full_path()
        validated_data["fellow_type"] = "M" if _apply_path.endswith("member/") else "L"
        return super().create(validated_data)

    def validatxe_provider(self, provider_id):
        """Validator provider"""
        try:
            _p = Provider.objects.get(id=provider_id)
            if is_supported_provider(_p):
                return provider_id
            raise NotSupportedProviderException()
        except Provider.DoesNotExist as provider_error:
            raise NotFoundProviderException() from provider_error


class ApplyCancelSerializer(serializers.Serializer):
    """Leader Cancel Serializer for View Response"""

    user_id = serializers.IntegerField()
    provider_id = serializers.IntegerField()

    def update(self, instance, validated_data):
        """Not used"""

    def create(self, validated_data):
        """Not used"""


class ApplyDetailSerializer(serializers.Serializer):
    """Abstract apply model serializer"""

    def update(self, instance, validated_data):
        """Not used"""

    def create(self, validated_data):
        """Not used"""

    fellows = serializers.ListField(child=FellowProfileSerializer(), default=[])
    provider = serializers.SerializerMethodField()
    time_stamps = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()

    def get_provider(self, obj):
        """Get provider data using ProviderSerializer"""
        return ProviderSerializer(obj.provider).data

    def get_status(self, obj):
        """Get default group status - <Recruiting>"""
        return "Recruiting"

    def get_time_stamps(self, obj):
        """Get time stamps"""
        return {"apply_date_time": obj.apply_date_time}
