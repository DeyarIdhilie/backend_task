from django.contrib import admin
from django.urls import path, include
from rest_framework_nested import routers
from .views.log_in_controller import LogInViewSet, LogoutView
from .views.movie_controller import MovieViewSet
from .views.actor_controller import ActorViewSet
from .views.trailer_controller import TrailerViewSet
from .views.user_controller import UserViewSet

router = routers.SimpleRouter()
router.register(r'movies', MovieViewSet, basename= 'movies')
router.register(r'actors', ActorViewSet, basename= 'actors')
router.register(r'users',UserViewSet, basename='user-register')
router.register(r'login',LogInViewSet, basename='user-login')
router.register(r'logout',LogoutView, basename='user-logout')
domains_router = routers.NestedSimpleRouter(router, r'movies', lookup='domain')
domains_router.register(r'trailers', TrailerViewSet, basename='movie-trailer')
# 'basename' is optional. Needed only if the same viewset is registered more than once
# Official DRF docs on this option: http://www.django-rest-framework.org/api-guide/routers/

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include(domains_router.urls)),
]




