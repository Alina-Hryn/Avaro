from django_filters import rest_framework as filters
from avaroapp.views import Movie


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class MovieFilter(filters.FilterSet):
    id = CharFilterInFilter(field_name='id', lookup_expr='in')

    class Meta:
        model = Movie
        fields = ['id', 'year']
