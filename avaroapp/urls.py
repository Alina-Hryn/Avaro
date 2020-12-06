from django.urls import path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('movies', MovieViewSet, 'movie')
router.register('cinemas', CinemaViewSet, 'cinema')
router.register('seances', SeanceViewSet, 'seance')

urlpatterns = router.urls
