# Generated by Django 4.0.4 on 2022-05-30 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tv_details', '0004_alter_tvseasondetail_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tvseasondetail',
            name='video',
        ),
    ]
