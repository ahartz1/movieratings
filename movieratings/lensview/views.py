from django.db.models import Avg, Count
from django.shortcuts import render
from .models import Rater, Movie

# Create your views here.


def movie_detail(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    ratings = movie.rating_set.all()
    return render(request,
                  'lensview/movie_detail.html',
                  {'movie': movie,
                   'ratings': ratings})


def user_detail(request, rater_id):
    rater = Rater.objects.get(pk=rater_id)
    ratings = rater.rating_set.all().order_by('-stars')
    return render(request,
                  'lensview/user_detail.html',
                  {'rater': rater,
                   'ratings': ratings})


def top_20(request):
    # First, make a list of movies that have more than 150 ratings
    popular_movies = Movie.objects.annotate(num_raters=Count('rating')).filter(
        num_raters__gte=150)

    # Next, look at all ratings, calculate average for each movie,
    # order by new field 'avg_rating'
    top_movies = popular_movies.annotate(avg_rating=Avg('rating__stars')) \
        .order_by('-avg_rating')[:20]

    return render(request,
                  'lensview/top_20.html',
                  {'top_movies': top_movies})
