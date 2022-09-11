from django.shortcuts import get_object_or_404
from rest_framework.parsers import FileUploadParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from ..utils.serializers.image_serializer import ImageSerializer
from ..models.movie import Movie
from ..models.image import Image
import os
from ..utils.custome_premissions import CustomPermissions


class ImageViewSet(ViewSet):
    parser_classes = (MultiPartParser,)
    permission_classes = [CustomPermissions]

    def list(self, request, domain_pk=None):
        movies = Movie.objects.all()
        the_movie = get_object_or_404(movies, pk=domain_pk)
        movie_images = Image.objects.filter(movie=the_movie)
        result = ImageSerializer(movie_images, many=True)
        return Response(data=result.data, status=200)

    def create(self, request, domain_pk=None, format=None):
        image = request.FILES['image']
        type = request.data.get("type")
        movies = Movie.objects.all()
        movie = get_object_or_404(movies, pk=domain_pk)
        if movie:
            is_there_cover = Image.objects.filter(movie=movie, type=1)
        if is_there_cover and type == '1':
            response = Response(status=400)
        else:
            destination = open(
                '/Users/lenovo/PycharmProjects/backend/movie_library_api/movie_library/images/' + image.name,
                'wb+')
            for chunk in image.chunks():
                destination.write(chunk)
            destination.close()
            path = 'C:/Users/lenovo/PycharmProjects/backend/movie_library_api/movie_library/images/' + image.name
            save_image = Image(movie=movie, uploaded_image=path, type=type)
            save_image.save()
            result = ImageSerializer(save_image)
            response = Response(data=result.data, status=201)
        return response

    def retrieve(self, request, domain_pk=None, pk=None):
        movies = Movie.objects.all()
        the_movie = get_object_or_404(movies, pk=domain_pk)
        images = Image.objects.all()
        the_image = get_object_or_404(images, pk=pk, movie=the_movie)
        result = ImageSerializer(the_image, many=False)
        return Response(data=result.data, status=200)

    def destroy(self, request, domain_pk=None, pk=None):
        movies = Movie.objects.all()
        the_movie = get_object_or_404(movies, pk=domain_pk)
        images = Image.objects.all()
        the_image = get_object_or_404(images, pk=pk, movie=the_movie)
        the_image.delete()
        try:
            if os.path.exists(the_image.uploaded_image):
                os.remove(the_image.uploaded_image)
                response = Response(status=204)
        except:
            response = Response(status=400)
        return response

    def update(self,request, domain_pk=None, pk=None ):
        movies = Movie.objects.all()
        movie = get_object_or_404(movies, pk=domain_pk)
        images = Image.objects.all()
        old_image = get_object_or_404(images, pk=pk)
        new_image = request.FILES['image']
        data = request.data
        type = data['type']
        if movie:
            is_there_cover = Image.objects.filter(movie=movie, type=1)
        if is_there_cover and type == '1':
            response = Response(status=400)
        else:
            try:
                if os.path.exists(old_image.uploaded_image):
                    os.remove(old_image.uploaded_image)
                    response = Response(status=204)
            except:
                response = Response(status=400)
            destination = open(
                '/Users/lenovo/PycharmProjects/backend/movie_library_api/movie_library/images/' + new_image.name,
                'wb+')
            for chunk in new_image.chunks():
                destination.write(chunk)
            destination.close()
            path = 'C:/Users/lenovo/PycharmProjects/backend/movie_library_api/movie_library/images/' + new_image.name
            old_image.uploaded_image = path
            old_image.type = type
            old_image.save()
            result = ImageSerializer(old_image)
            response = Response(data=result.data, status=200)
        return response
