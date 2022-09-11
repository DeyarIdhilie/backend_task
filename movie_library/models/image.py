from .base_model import BaseModel
from django.db import models
from .movie import Movie
class Image(BaseModel):
    class Meta:
        db_table = "image"

    class Type(models.IntegerChoices):
        COVER = 1
        OTHER = 2

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="images")
    uploaded_image = models.CharField(max_length=300, unique=True, blank=True, null=True)
    type = models.IntegerField(choices=Type.choices, default=2)
