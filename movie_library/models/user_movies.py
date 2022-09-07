from django.db import models
from .movie import Movie
from .users import CustomUser
from .base_model import BaseModel


class UserMovies(BaseModel):
    class Meta:
        db_table = "user_movie"

    users= models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="movies")
    movies = models.ForeignKey(Movie, on_delete= models.CASCADE, related_name="users")
