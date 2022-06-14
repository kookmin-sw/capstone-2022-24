# Generated by Django 4.0.4 on 2022-05-31 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0007_alter_provider_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscriptiontype',
            name='number_of_subscribers',
        ),
        migrations.AddField(
            model_name='charge',
            name='number_of_subscribers',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]