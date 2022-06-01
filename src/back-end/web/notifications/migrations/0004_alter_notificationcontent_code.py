# Generated by Django 4.0.4 on 2022-06-02 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0003_notification_deadline_date_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notificationcontent',
            name='code',
            field=models.CharField(choices=[('P001', '토스 결제 완료'), ('G001', '신청 완료'), ('G002', '모집 완료'), ('G003', '검토 요청'), ('G004', '관람 기간'), ('G005', '연장 취소'), ('G006', '구독 연장'), ('G007', '모임 연장'), ('G008', '해체 처리'), ('G009', '관람 종료'), ('A001', '계정 대기'), ('A002', '등록 요청'), ('A002', '정보 변경'), ('R001', '모임장 신고'), ('R002', '모임 신고'), ('R003', '모임장 신고 취소'), ('R004', '모임 신고 취소'), ('M001', '사용 완료'), ('M002', '적립 완료'), ('M003', '환급 완료')], max_length=4),
        ),
    ]