from django.contrib import admin
from django.urls import path, include


from rest_framework import routers
#from rest_framework.routers import ExtendedSimpleRouter
#from third_party_app.routers import SomeRouter

from .views.movie_controller import MovieViewSet
from .views.actor_controller import ActorViewSet
router = routers.SimpleRouter()

router.register(r'movies', MovieViewSet, basename="library_movies")
router.register(r'actors', ActorViewSet, basename="actors")
'''router = ExtendedSimpleRouter()
# tasks route
(
    router.register(r'tasks', TaskViewSet)
          .register(r'comments',
                    CommentViewSet,
                    'tasks-comment',
                    parents_query_lookups=['object_id'])
)'''
urlpatterns = router.urls