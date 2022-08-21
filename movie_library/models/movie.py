from django.db import models
from .actor import Actor

class Movie(models.Model):
    class Meta:

        db_table = "movie"

    title = models.CharField(max_length=30)
    year = models.CharField(max_length=4)
    duration = models.IntegerField()
    release_date = models.DateField()
    actors = models.ManyToManyField(Actor)
    #cover_image = models.ImageField(null=True, blank=True, upload_to="images/")

    #objects = models.Manager()