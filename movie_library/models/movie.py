from django.db import models
from .actor import Actor
from .base_model import BaseModel

#from .trailer import Trailer
class Movie(BaseModel):
    class Meta:

        db_table = "movie"

    title = models.CharField(max_length=100)
    year = models.CharField(max_length=4)
    duration = models.IntegerField()
    release_date = models.DateField()
    actors = models.ManyToManyField(Actor)
   #cover_image = models.ImageField(null=True, blank=True, upload_to="images/")
    '''def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.trailer_set = None'''

    @property
    def trailers(self):
        return Movie.trailers.all()


    #objects = models.Manager()

