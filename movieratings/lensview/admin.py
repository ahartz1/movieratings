from django.contrib import admin
from .models import Rater, Movie, Rating


class RaterAdmin(admin.ModelAdmin):
    list_display = ['id', 'age', 'gender']

# Register your models here.
admin.site.register(Rater)
admin.site.register(Movie)
admin.site.register(Rating)
