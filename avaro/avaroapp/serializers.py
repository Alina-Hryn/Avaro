from rest_framework import serializers
from .models import Movie, Cinema, Seance, CinemaMovie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'year', 'category', 'genre', 'duration')


class MovieDetailSerializer(serializers.ModelSerializer):
    # category = serializers.SlugRelatedField(slug_field="name", read_only=True)
    # directors = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    # actors = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    # genres = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    class Meta:
        model = Movie
        exclude = ("genre",)


class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = '__all__'


class CinemaMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaMovie
        fields = '__all__'


class SeanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seance
        fields = '__all__'
