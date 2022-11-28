from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import *

movie_router = SimpleRouter()
movie_router.register(prefix='movies', viewset=MovieViewSet)
print(movie_router.urls)
director_router = SimpleRouter()
director_router.register(prefix='directors', viewset=DirectorViewSet)

review_router = SimpleRouter()
review_router.register(prefix='reviews', viewset=ReviewViewSet)

urlpatterns = [
    path('', include(movie_router.urls)),
    path('', include(director_router.urls)),
    path('', include(review_router.urls))
]