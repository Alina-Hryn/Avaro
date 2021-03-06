# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy_djangoitem import DjangoItem
from avaroapp.models import Movie, Seance, CinemaMovie


class MovieItem(DjangoItem):
    django_model = Movie


class CinemaMovieItem(DjangoItem):
    django_model = CinemaMovie


class SeanceItem(DjangoItem):
    django_model = Seance
