from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import *

movie_router = SimpleRouter()
movie_router.register(prefix='movies', viewset=MovieViewSet)

director_router = SimpleRouter()
director_router.register(prefix='directors', viewset=DirectorViewSet)

review_router = SimpleRouter()
review_router.register(prefix='reviews', viewset=ReviewViewSet)

urlpatterns = [
    path('movies/reviews/', movies_reviews_view),
    path('', include(movie_router.urls)),
    path('', include(director_router.urls)),
    path('', include(review_router.urls))
]