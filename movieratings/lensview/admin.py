from django.contrib import admin
from .models import Rater, Movie

# Register your models here.
class RaterAdmin(admin.ModelAdmin):
    display_list = ['gender', 'age', 'occupation', 'zipcode', 'user__username']


class MovieAdmin(admin.ModelAdmin):
    display_list = ['title', 'genres']

admin.site.register(Rater, RaterAdmin)
admin.site.register(Movie, MovieAdmin)
