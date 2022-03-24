# Generated by Django 4.0.3 on 2022-03-24 21:44

from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SocialType',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('logo_key', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=50)),
                ('withdrawal_date_time', models.DateTimeField(db_column='withdrawalDateTime', default=None, null=True)),
            ],
        ),
    ]
