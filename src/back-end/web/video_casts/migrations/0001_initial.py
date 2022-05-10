# Generated by Django 4.0.4 on 2022-05-11 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoCast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('department', models.CharField(choices=[('CS', 'Cast'), ('CR', 'Crew'), ('SD', 'Sound'), ('LG', 'Lighting'), ('PD', 'Production'), ('AT', 'Art'), ('ED', 'Editing'), ('CM', 'Costume & Make-Up'), ('CR', 'Camera'), ('DR', 'Directing'), ('VE', 'Visual Effects'), ('AC', 'Actors'), ('WR', 'Writing')], max_length=2, null=True)),
                ('role', models.CharField(max_length=50, null=True)),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videos.video')),
            ],
            options={
                'db_table': 'video_casts',
            },
        ),
    ]
