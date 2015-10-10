from django.shortcuts import render
from .models import Movie

# Create your views here.


def movie_detail(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    ratings = movie.rating_set.all()
    return render(request,
                  'lensview/movie_detail.html',
                  {'movie': movie,
                   'ratings': ratings})
