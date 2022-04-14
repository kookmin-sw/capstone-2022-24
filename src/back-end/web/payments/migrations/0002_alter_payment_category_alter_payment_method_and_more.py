# Generated by Django 4.0.3 on 2022-04-14 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='category',
            field=models.CharField(choices=[('N', 'NORMAL'), ('B', 'BILLING'), ('C', 'CONNECTPAY')], max_length=1),
        ),
        migrations.AlterField(
            model_name='payment',
            name='method',
            field=models.CharField(choices=[('C', 'CARD'), ('VA', 'VIRTUAL_ACCOUNT'), ('CP', 'CELL_PHONE'), ('AT', 'ACCOUNT_TRANSFER'), ('V', 'VOUCHER')], max_length=2),
        ),
        migrations.AlterField(
            model_name='payment',
            name='status',
            field=models.CharField(choices=[('R', 'READY'), ('I', 'IN_PROGRESS'), ('W', 'WAITING_FOR_DEPOSIT'), ('D', 'DONE'), ('C', 'CANCELED'), ('P', 'PARTIAL_CANCELED'), ('A', 'ABORTED'), ('E', 'EXPIRED')], default='r', max_length=1),
        ),
    ]
