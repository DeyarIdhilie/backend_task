import base64

import jwt
from django.conf import settings
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework_simplejwt.tokens import Token
from rest_framework_simplejwt.models import TokenUser
from ..models.users import CustomUser
from ..utils.serializers.register_serializer import RegisterSerializer
from ..utils.user_permissions import UserPermissions
from ..models.user_movies import UserMovies
from ..utils.serializers.user_movies_serializer import UserMoviesSerializer
from ..models.movie import Movie
from ..utils.serializers.movie_serializer import MovieSerializer
from ..utils.serializers.movie_serializer import MovieTrailerSerializer
class UserMoviesViewSet(ViewSet):
    #permission_classes = [UserPermissions, ]

    def create(self, request, domain_pk=None):
        data = request.data
        movies_in = data.get('movies')
        user_id = domain_pk
        user = CustomUser.objects.get(id=user_id)
        response = Response(status=403)
        if UserPermissions().check_object_permissions(request, user):
            movies_query = Movie.objects.all()
            for movie_id in movies_in:
                movie = get_object_or_404(movies_query, pk=movie_id)
                user_movie_library = UserMovies(users=user, movies=movie)
                user_movie_library.save()

            user_movies = UserMovies.objects.filter(users=user_id)
            result = UserMoviesSerializer(user_movies, many=True)
            response = Response(data=result.data, status=201)
        return response

    def list(self, request, domain_pk=None):
        user = CustomUser.objects.get(id=domain_pk)
        response= Response(status=403)
        if UserPermissions().check_object_permissions(request, user):
            user_movies = UserMovies.objects.filter(users=user)
            result = UserMoviesSerializer(user_movies, many=True)
            response= Response(data=result.data, status=200)
        return response

    def retrieve(self, request, pk=None, domain_pk=None):
        user = CustomUser.objects.get(id=domain_pk)
        response = Response(status=403)
        if UserPermissions().check_object_permissions(request, user):
            user_movie = UserMovies.objects.get(pk=pk, users=user)
            movie_in_row = user_movie.movies
            result = MovieTrailerSerializer(movie_in_row)
            response = Response(data=result.data, status=204)
        return response

    def update(self, request, pk=None, domain_pk=None):
        user = CustomUser.objects.get(id=domain_pk)
        response = Response(status=403)
        if UserPermissions().check_object_permissions(request, user):
            data = request.data
            new_movie_id = data.get("movies")
            user_movie = UserMovies.objects.get(pk=pk)
            movie = Movie.objects.get(pk=new_movie_id)
            user_movie.movies = movie
            result = UserMoviesSerializer(user_movie)
            response = Response(data=result.data, status=200)
        return response

    def partial_update(self, request, pk=None, domain_pk=None):
        pass

    def destroy(self, request, pk=None, domain_pk=None):
        user = CustomUser.objects.get(id=domain_pk)
        response = Response(status=403)
        if UserPermissions().check_object_permissions(request, user):
            # movies = Movie.objects.all()
            # movie = get_object_or_404(movies, pk=pk)
            # user_movie = UserMovies.objects.get(users=user,movies=movie)
            user_movie = UserMovies.objects.get(pk=pk, users=user)
            user_movie.delete()
            response = Response(status=204)
        return response
