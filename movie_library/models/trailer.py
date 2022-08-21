from django.db import models
from .movie import Movie

class Trailer(models.Model):


       movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
       url = models.URLField(
              max_length=200,
              db_index=True,
              unique=True,
              blank=True
       )

       def __str__(self):
              return self.movie.title