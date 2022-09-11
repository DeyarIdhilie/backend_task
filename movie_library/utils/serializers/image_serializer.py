from rest_framework.serializers import ModelSerializer
from ...models.image import Image


class ImageSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'movie', 'uploaded_image', 'created', 'updated', 'type']