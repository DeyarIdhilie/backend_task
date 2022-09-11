from django.db import models
from .base_model import BaseModel


class Movie(BaseModel):
    class Meta:
        db_table = "movie"

    title = models.CharField(max_length=100)
    year = models.CharField(max_length=4)
    duration = models.IntegerField()
    release_date = models.DateField()
    #actors = models.ManyToManyField(Actor, through='MovieActor')


    def __str__(self):
        return self.title