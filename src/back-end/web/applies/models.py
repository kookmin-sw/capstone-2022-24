"""Model definition of applies application: BaseApply(Abstract), LeaderApply, MemberApply"""
from django.conf import settings
from django.db import models
from django.utils import timezone
from payments.models import Payment
from providers.models import Provider


class BaseApply(models.Model):
    """Abstract model definition about Common part of apply"""

    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, null=False, on_delete=models.CASCADE)
    provider = models.ForeignKey(Provider, null=False, on_delete=models.CASCADE)
    apply_date_time = models.DateTimeField(default=timezone.now)

    class Meta:
        """Abstract setting obout BaseApply model"""

        abstract = True

    def __str__(self):
        return f"[{self.provider.name}] {self.user.name}님의 구성원 신청"


class LeaderApply(BaseApply):
    """Model definition of applying group to Leader"""

    class Meta:
        """Metadata of LeaderApply model"""

        db_table = "leader_apply"
        verbose_name_plural = "Leader applies"
        ordering = ("-apply_date_time",)

    def __str__(self):
        return f"[{self.provider}] {self.user}님의 모임장 신청"


class MemberApply(BaseApply):
    """Model definition of applying group to member"""

    class Meta:
        """Metadata of MemberApply model"""

        db_table = "member_apply"
        verbose_name_plural = "Member applies"
        ordering = ("-apply_date_time",)

    def __str__(self):
        return f"[{self.provider}] {self.user}님의 모임원 신청"
