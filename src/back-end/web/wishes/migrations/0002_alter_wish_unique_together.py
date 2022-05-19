# Generated by Django 4.0.4 on 2022-05-17 18:08

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wishes', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='wish',
            unique_together={('user', 'video')},
        ),
    ]
