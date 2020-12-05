# Generated by Django 3.1.4 on 2020-12-05 01:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('avaroapp', '0004_auto_20201205_0225'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cinemamovie',
            name='high_price',
        ),
        migrations.RemoveField(
            model_name='seance',
            name='cinema_movie',
        ),
        migrations.AddField(
            model_name='seance',
            name='cinema_movie_id',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='avaroapp.cinemamovie'),
        ),
        migrations.AlterField(
            model_name='cinema',
            name='address',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='cinema',
            name='link',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='cinemamovie',
            name='cinema_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='avaroapp.cinema'),
        ),
        migrations.AlterField(
            model_name='cinemamovie',
            name='end_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='cinemamovie',
            name='movie_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='avaroapp.movie'),
        ),
        migrations.AlterField(
            model_name='cinemamovie',
            name='start_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='category',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='duration',
            field=models.TimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='movie',
            name='rating',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='release',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='trailer',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='seance',
            name='date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='seance',
            name='high_price',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='seance',
            name='low_price',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='seance',
            name='time',
            field=models.TimeField(blank=True),
        ),
    ]