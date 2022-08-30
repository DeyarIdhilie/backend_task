from django.db import models
from .movie import Movie
from .actor import Actor
from .base_model import BaseModel


class MovieActor(BaseModel):
    class Meta:
        db_table = "movie_actor"

    actors = models.ForeignKey(Actor, on_delete=models.CASCADE)
    movies = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="actors")
