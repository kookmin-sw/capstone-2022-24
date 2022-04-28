# Generated by Django 4.0.3 on 2022-04-28 21:43

from django.db import migrations, models
import django.db.models.deletion
import djongo.models.fields
import videos.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('tmdb_id', models.BigIntegerField(db_column='tmdbId', null=True)),
                ('title', models.CharField(max_length=200, null=True)),
                ('release_date', models.DateField(db_column='releaseDate')),
                ('film_rating', models.CharField(db_column='filmRating', max_length=10)),
                ('category', models.CharField(choices=[('TV', 'TVSeries'), ('MV', 'Movie')], max_length=2, null=True)),
                ('poster_key', models.ImageField(db_column='posterKey', upload_to='')),
                ('title_english', models.CharField(db_column='titleEnglish', max_length=200)),
            ],
            options={
                'db_table': 'videos',
            },
        ),
        migrations.CreateModel(
            name='VideoDetail',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('runtime', models.IntegerField()),
                ('ratings', djongo.models.fields.ArrayField(model_container=videos.models.Rating)),
                ('production_countries', djongo.models.fields.ArrayField(db_column='productionCountries', model_container=videos.models.ProductionCountry)),
                ('gernes', djongo.models.fields.ArrayField(max_length=50, model_container=videos.models.Gerne, null=True)),
                ('video', models.ForeignKey(db_column='videoId', on_delete=django.db.models.deletion.CASCADE, to='videos.video')),
            ],
            options={
                'db_table': 'video_details',
            },
        ),
    ]
