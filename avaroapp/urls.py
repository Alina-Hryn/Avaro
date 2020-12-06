from rest_framework import routers
from .api import MovieViewSet


router = routers.DefaultRouter()
router.register('api/movie', MovieViewSet, 'movie')

urlpatterns = router.urls
