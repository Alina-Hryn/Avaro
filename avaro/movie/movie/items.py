# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy_djangoitem import DjangoItem
from avaroapp.models import Movie, Cinema


class MovieItem(DjangoItem):
    django_model = Movie


class CinemaItem(DjangoItem):
    django_model = Cinema
