from django.db import models
#from .movie import Movie
from .base_model import BaseModel


class Actor(BaseModel):

    class Meta:

       db_table = "actor"

    class Gender(models.TextChoices):
        FEMALE = 'Female'
        MALE = 'Male'
        OTHER = 'Others'

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=6, choices=Gender.choices, default=Gender.FEMALE,)
    #movies = models.ManyToManyField(Movie)

    '''def show_movies(self):
        return Actor_Movie.objects.filter(actors=self)'''

    def __str__(self):
          return f"{self.first_name} {self.last_name}"


'''class Actor_Movie(models.Model):
    class Meta:

        db_table = "actor_movie"

    actors = models.ForeignKey(Actor, on_delete=models.DO_NOTHING)
    movies = models.ForeignKey(Movie, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.actors.first_name}, " \
               f"${self.movies.title}"'''