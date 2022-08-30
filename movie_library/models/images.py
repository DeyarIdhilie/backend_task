from django.db import models
from .movie import Movie
from .base_model import BaseModel


class Image(BaseModel):
    class Meta:
        db_table = "image"

    class Type(models.IntegerChoices):
        COVER = 1
        OTHER = 2


    movie = models.ForeignKey(Movie, on_delete=models.CASCADE,related_name="images")
    url = models.ImageField(null=True, blank=True,
                            upload_to="images/")  # todo change to use string instead of image field
    type = models.IntegerField(choices=Type.choices)

    def __str__(self):
        return self.title
