from rest_framework import routers
from .api import MovieViewSet, CinemaViewSet


router = routers.DefaultRouter()
router.register('movies', MovieViewSet, 'movie')
router.register('cinemas', CinemaViewSet, 'cinema')

urlpatterns = router.urls

