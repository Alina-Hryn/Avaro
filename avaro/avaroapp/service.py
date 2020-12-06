from django_filters import rest_framework as filters
from avaroapp.views import Movie, Cinema


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class CinemaFilter(filters.FilterSet):
    id = CharFilterInFilter(field_name='id', lookup_expr='in')

    class Meta:
        model = Cinema
        fields = ['id', 'cinema_network']


class MovieFilter(filters.FilterSet):
    id = CharFilterInFilter(field_name='id', lookup_expr='in')

    class Meta:
        model = Movie
        fields = ['id', 'year']
