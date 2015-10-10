from django.shortcuts import render
from .models import Rater, Movie, Rating

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


# def top_20(request):
#     top_movies = Rating.objects.all().order_by('')
#     # look at all ratings, 
