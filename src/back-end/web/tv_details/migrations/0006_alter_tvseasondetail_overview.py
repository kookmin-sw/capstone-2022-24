# Generated by Django 3.2.13 on 2022-06-01 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tv_details', '0005_remove_tvseasondetail_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tvseasondetail',
            name='overview',
            field=models.TextField(blank=True, null=True),
        ),
    ]