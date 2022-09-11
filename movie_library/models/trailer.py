from django.db import models
from .movie import Movie
from .base_model import BaseModel


class Trailer(BaseModel):
    class Meta:
        db_table = "trailer"

    movies = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="trailers")
    url = models.URLField(
        max_length=200,
        db_index=True,
        unique=True,
        blank=True
    )
    # you should use db_index=True when you have a field that is unique for faster lookups.

    def __str__(self):
        return self.movie.title
