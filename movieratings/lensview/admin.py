from django.contrib import admin
from .models import Rater, Movie, Rating


class RaterAdmin(admin.ModelAdmin):
    display_list = ['gender', 'age', 'occupation', 'zipcode', 'user__username']


class MovieAdmin(admin.ModelAdmin):
    display_list = ['title', 'genres']


class RatingAdmin(admin.ModelAdmin):
    display_list = ['rater__user__username', 'stars', 'movie__title']


# Register your models here.
admin.site.register(Rater, RaterAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Rating, RatingAdmin)
