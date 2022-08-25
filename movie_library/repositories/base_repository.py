from ..models import *
class BaseRepository():

    def get_base_query(self, model=None, filters=None, **options):
        return model.objects.all()