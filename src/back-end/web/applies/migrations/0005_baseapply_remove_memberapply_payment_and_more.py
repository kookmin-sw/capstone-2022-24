# Generated by Django 4.0.4 on 2022-05-23 03:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
        ('providers', '0007_alter_provider_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('applies', '0004_alter_leaderapply_payment_alter_memberapply_payment'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseApply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apply_date_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('payment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='payments.payment')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='providers.provider')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-apply_date_time',),
                'unique_together': {('user', 'provider')},
            },
        ),
        migrations.RemoveField(
            model_name='memberapply',
            name='payment',
        ),
        migrations.RemoveField(
            model_name='memberapply',
            name='provider',
        ),
        migrations.RemoveField(
            model_name='memberapply',
            name='user',
        ),
        migrations.DeleteModel(
            name='LeaderApply',
        ),
        migrations.DeleteModel(
            name='MemberApply',
        ),
        migrations.CreateModel(
            name='LeaderApply',
            fields=[
            ],
            options={
                'verbose_name_plural': 'Leader applies',
                'db_table': 'leader_apply',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('applies.baseapply',),
        ),
        migrations.CreateModel(
            name='MemberApply',
            fields=[
            ],
            options={
                'verbose_name_plural': 'Member applies',
                'db_table': 'member_apply',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('applies.baseapply',),
        ),
    ]