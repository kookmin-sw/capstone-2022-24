# Generated by Django 4.0.4 on 2022-05-01 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tmdb_id', models.BigIntegerField(null=True)),
                ('title', models.CharField(max_length=200, null=True)),
                ('release_date', models.DateField()),
                ('film_rating', models.CharField(max_length=10)),
                ('category', models.CharField(choices=[('TV', 'TVSeries'), ('MV', 'Movie')], max_length=2, null=True)),
                ('poster_key', models.ImageField(null=True, upload_to='')),
                ('title_english', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'videos',
            },
        ),
        migrations.CreateModel(
            name='VideoDetail',
            fields=[
                ('video_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='videos.video')),
                ('runtime', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'video_details',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('value', models.FloatField(max_length=10)),
                ('video_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videos.videodetail')),
            ],
            options={
                'db_table': 'ratings',
            },
        ),
        migrations.CreateModel(
            name='ProductionCountry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2)),
                ('video_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videos.videodetail')),
            ],
            options={
                'db_table': 'production_countries',
            },
        ),
        migrations.CreateModel(
            name='Gerne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('video_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videos.videodetail')),
            ],
            options={
                'db_table': 'gernes',
            },
        ),
    ]
