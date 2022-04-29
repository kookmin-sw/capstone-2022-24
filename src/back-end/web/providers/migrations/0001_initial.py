# Generated by Django 4.0.4 on 2022-04-26 18:38

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tmdb_id', models.PositiveBigIntegerField()),
                ('name', models.CharField(choices=[('NF', 'Netflix'), ('WC', 'Watcha'), ('DP', 'DisneyPlus'), ('TV', 'Tving'), ('WV', 'Wavve'), ('AP', 'AmazonPrime')], max_length=2)),
                ('logo_key', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'provider',
            },
        ),
        migrations.CreateModel(
            name='SubscriptionType',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('number_of_subscribers', models.PositiveSmallIntegerField()),
                ('detail', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'subscription_type',
            },
        ),
        migrations.CreateModel(
            name='Charge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_charge_per_member', models.PositiveIntegerField(default=0)),
                ('subscription_charge_per_member', models.PositiveIntegerField(default=0)),
                ('total_subscription_charge', models.PositiveIntegerField(default=0)),
                ('base_date', models.DateField(default=django.utils.timezone.now)),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='providers.provider')),
                ('subscription_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='providers.subscriptiontype')),
            ],
            options={
                'db_table': 'charge',
            },
        ),
    ]
