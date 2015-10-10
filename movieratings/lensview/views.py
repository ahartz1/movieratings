from django.shortcuts import render
from .models import Movie

# Create your views here.


def movie_detail(request, movie_id):
    movie = Movie.objects.filter(pk=movie_id)
    stars = u"\u2605" * (movie.average_rating() - 1)
    return render(request,
                  'lensview/movie_detail.html',
                  {'movie': movie,
                   'stars': stars})
