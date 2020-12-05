# Generated by Django 3.1.4 on 2020-12-05 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avaroapp', '0005_auto_20201205_0346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='category',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='duration',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='movie',
            name='rating',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='release',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='trailer',
            field=models.URLField(blank=True, null=True),
        ),
    ]