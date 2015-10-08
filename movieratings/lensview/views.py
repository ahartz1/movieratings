from django.shortcuts import render
from django.db.models import Avg
# from django.http import HttpResponse
# from .models import Rater, Movie, Rating
from .models import Movie, Rater


# Create your views here.
def top_20(request):
    movies = Movie.objects.annotate(Avg('rating__stars')) \
        .order_by('-rating__stars__avg')[:20]

    return render(request,
                  'lensview/top_20.html',
                  {'movies': movies})


def show_movie(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    ratings = movie.rating_set.all()
    return render(request,
                  'lensview/movie.html',
                  {'movie': movie,
                   'ratings': ratings})


def show_rater(request, rater_id):
    rater = Rater.objects.get(pk=rater_id)
    # ratings = rater.rating_set.all()
    movie_ratings = []
    for rating in rater.rating_set.all():
        movie_ratings.append({
            'movie': rating.movie,
            'stars': '\u2605' * rating.stars
        })
    return render(request,
                  'lensview/rater.html',
                  {'rater': rater,
                   'movie_ratings': movie_ratings})
