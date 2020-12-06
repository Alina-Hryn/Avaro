from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from rest_framework import viewsets, permissions, generics, mixins
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from .service import *


class MovieViewSet(viewsets.ModelViewSet):
    filter_backends = (DjangoFilterBackend,)
    filterset_class = MovieFilter
    filterset_fields = ['id', 'year']
    queryset = Movie.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = MovieSerializer


class CinemaViewSet(viewsets.ModelViewSet):
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CinemaFilter
    queryset = Cinema.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CinemaSerializer


class CinemaMovieViewSet(viewsets.ModelViewSet):
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CinemaMovieFilter
    queryset = CinemaMovie.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CinemaMovieSerializer


class SeanceViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = Seance.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SeanceSerializer
