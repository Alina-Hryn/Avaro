from django.db import models


# Create your models here.

class Cinema(models.Model):
    cinema_network = models.CharField(max_length=150, blank= True, null=True)
    location = models.CharField(max_length=150)
    address = models.TextField(blank=True)

    link = models.URLField(max_length=200, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['cinema_network', 'name'], name='cinema_name')
        ]


class Movie(models.Model):
    title = models.CharField(max_length=150, unique=True)
    year = models.IntegerField(blank=True, default=2020)
    category = models.IntegerField(blank=True, null=True)
    genre = models.IntegerField(blank=True, null=True)
    duration = models.TimeField(blank=True, null=True)
    release = models.DateField(blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    photo = models.ImageField(blank=True,null=True)
    trailer = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    link = models.URLField(max_length=200, blank=True, null=True)


class CinemaMovie(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    cinema_id = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)

    link = models.URLField(max_length=200, blank=True)


class Seance(models.Model):
    cinema_movie_id = models.ForeignKey(CinemaMovie, on_delete=models.CASCADE, blank=True, default=None)
    date = models.DateField(blank=True)
    time = models.TimeField(blank=True)
    low_price = models.FloatField(blank=True)
    high_price = models.FloatField(blank=True)

    link = models.URLField(max_length=200, blank=True)
