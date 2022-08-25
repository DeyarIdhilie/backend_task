from django.contrib import admin
from .models.movie import *

# Register your models here.
from .models.movie import Movie
from .models.actor import *
from .models.trailer import Trailer
#from .models.actor
admin.site.register(Movie)
#.site.register(Actor)
admin.site.register(Trailer)

'''class trailorInline(admin.StackedInline):
    model = Trailer
    extra = 0'''
#@admin.register(Movie)
'''class movieAdmin(admin.ModelAdmin):
    inlines = [trailorInline]# , actorInline]
    #list_display = ["created", "total_price", "paid"]
    
admin.site.register(Movie,movieAdmin)
admin.site.register(Actor)#,actorAdmin)'''


'''class actorInline(admin.StackedInline):
    model = Actor_Movie
    extra = 0


class movieInline(admin.StackedInline):
    model = Actor_Movie
    extra = 0'''



'''class actorAdmin(admin.ModelAdmin):
    inlines = [movieInline]'''
''' list_display = ("show_average",)
    def show_average(self, obj):

        result = Actor_Movie.objects.filter(actors=obj)
        return result'''




