from django.contrib import admin
from .models import Rater, Movie, Rating


class RaterAdmin(admin.ModelAdmin):
    list_display = ['id', 'age', 'gender']

class MovieAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'average_rating']

class RatingAdmin(admin.ModelAdmin):
    list_display = ['id', 'rater', 'stars', 'movie']

# Register your models here.
admin.site.register(Rater, RaterAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Rating, RatingAdmin)
