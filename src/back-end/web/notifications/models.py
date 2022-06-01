"""Definitions of notification models: NotificationContent, Notification"""
from django.conf import settings
from django.db import models
from django.utils import timezone
from providers.models import Provider


class NotificationContent(models.Model):
    """Definition of notification details model"""

    CODE_CHOICES = (
        ("P001", "결제 완료"),
        ("G001", "모임 신청 완료"),
        ("G002", "모집 완료"),
        ("G003", "검토 요청"),
        ("G004", "관람 기간"),
        ("G005", "연장 취소"),
        ("G006", "구독 연장"),
        ("G007", "모임 연장"),
        ("G008", "모임 해체"),
        ("G009", "모임 완주"),
        ("A001", "계정 대기"),
        ("A002", "계정 등록 요청"),
        ("R001", "모임장 신고"),
        ("R002", "모임 신고"),
        ("P002", "결제 요청"),
        ("M001", "마일리지 사용"),
        ("M002", "마일리지 적립"),
        # T0D0
    )
    code = models.CharField(max_length=4, choices=CODE_CHOICES)
    message = models.CharField(max_length=50)

    class Meta:
        """Metadata for notification_content model"""

        db_table = "notification_content"

    def __str__(self):
        return f"{self.keyword}: {self.message}"

    @property
    def keyword(self):
        """Notification header written in Korean"""
        return f"{self.get_code_display()}"[:20]


class Notification(models.Model):
    """Definition of notification relationship model"""

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    content = models.ForeignKey(NotificationContent, on_delete=models.CASCADE)
    has_read = models.BooleanField(default=False)
    creation_date_time = models.DateTimeField(
        default=timezone.now,
    )

    class Meta:
        """Metadata for notification model"""

        db_table = "notification"

    def __str__(self):
        return f"[{'읽음' if self.has_read else '안읽음'} 알림 #{self.id} ({self.creation_date_time})"
