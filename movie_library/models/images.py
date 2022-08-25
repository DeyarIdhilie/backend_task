from django.db import models
from .movie import Movie
from .base_model import BaseModel
class Image(BaseModel):
    class Meta:

        db_table = "image"

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    url = models.ImageField(null=True, blank=True, upload_to="images/")# todo change to use string instead of image field
    type = models.IntegerChoices

    def __str__(self):
        return self.title