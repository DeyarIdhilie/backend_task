from django.contrib import admin
from django.urls import path, include


from rest_framework import routers

from .views.movie_controller import MovieViewSet
from .views.actor_controller import ActorViewSet
router = routers.SimpleRouter()

router.register(r'movies', MovieViewSet, basename="library_movies")
router.register(r'actors', ActorViewSet, basename="actors")

urlpatterns = router.urls