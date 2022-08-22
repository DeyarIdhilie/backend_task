from django.db import models
from .movie import Movie
from .base_model import BaseModel
class Trailer(BaseModel):


       movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="trailer")
       url = models.URLField(
              max_length=200,
              db_index=True,
              unique=True,
              blank=True
       )

       def __str__(self):
              return self.movie.title