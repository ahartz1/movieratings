from django.contrib import admin
from .models import Rater, Movie, Rating


class RaterAdmin(admin.ModelAdmin):
    list_display = ('user', 'gender', 'age', 'occupation', 'zipcode')


class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'genres', 'average_rating')


class RatingAdmin(admin.ModelAdmin):
    list_display = ('rater_username', 'stars', 'movie_title')


# Register your models here.
admin.site.register(Rater, RaterAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Rating, RatingAdmin)
