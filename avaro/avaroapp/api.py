from .models import *
from rest_framework import viewsets, permissions
from .serializers import MovieSerializer, CinemaSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = MovieSerializer


class CinemaViewSet(viewsets.ModelViewSet):
    queryset = Cinema.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CinemaSerializer
