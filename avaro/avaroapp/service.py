from django_filters import rest_framework as filters
from avaroapp.views import Movie, Cinema, CinemaMovie


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


class CinemaMovieFilter(filters.FilterSet):
    # cinema_id = CharFilterInFilter(field_name='cinema__location', lookup_expr='in')
    # movie_id = CharFilterInFilter(field_name='movie__title', lookup_expr='in')

    class Meta:
        model = CinemaMovie
        fields = ['cinema_id', 'movie_id']
