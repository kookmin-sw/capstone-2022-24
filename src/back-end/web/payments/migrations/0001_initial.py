# Generated by Django 4.0.4 on 2022-05-03 22:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(default=0)),
                ('content', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('N', 'NORMAL'), ('B', 'BILLING'), ('C', 'CONNECTPAY')], max_length=1)),
                ('method', models.CharField(choices=[('C', 'CARD'), ('VA', 'VIRTUAL_ACCOUNT'), ('CP', 'CELL_PHONE'), ('AT', 'ACCOUNT_TRANSFER'), ('V', 'VOUCHER')], max_length=2)),
                ('status', models.CharField(choices=[('R', 'READY'), ('I', 'IN_PROGRESS'), ('W', 'WAITING_FOR_DEPOSIT'), ('D', 'DONE'), ('C', 'CANCELED'), ('P', 'PARTIAL_CANCELED'), ('A', 'ABORTED'), ('E', 'EXPIRED')], default='R', max_length=1)),
                ('request_date_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('approval_date_time', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'payment',
            },
        ),
    ]
