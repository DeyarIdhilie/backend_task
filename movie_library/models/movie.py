from django.db import models
from .actor import Actor
from .base_model import BaseModel


class Movie(BaseModel):
    class Meta:
        db_table = "movie"

    title = models.CharField(max_length=100)
    year = models.CharField(max_length=4)
    duration = models.IntegerField()
    release_date = models.DateField()
    actors = models.ManyToManyField(Actor)

    @property
    def trailers(self):
        return Movie.trailers.all()
