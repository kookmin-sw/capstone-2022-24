# Generated by Django 4.0.4 on 2022-05-21 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0005_alter_subscriptiontype_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provider',
            name='name',
            field=models.CharField(choices=[('NF', '넷플릭스'), ('WC', '왓챠'), ('DP', '디즈니 플러스'), ('TV', '티빙'), ('WV', '웨이브'), ('AP', '아마존 프라임')], max_length=2),
        ),
    ]