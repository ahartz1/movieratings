from django.contrib.auth import authenticate, login
from django.db.models import Avg, Count
# from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Movie, Rater


# Create your views here.
def top_20(request):

    popular_movies = Movie.objects.annotate(num_ratings=Count('rating')) \
        .filter(num_ratings__gte=50)

    movies = popular_movies.annotate(Avg('rating__stars')) \
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
            'stars': '\u2605' * (rating.stars - 1)
        })
    return render(request,
                  'lensview/rater.html',
                  {'rater': rater,
                   'movie_ratings': movie_ratings})


def user_login(request):
    if request.method == 'POST':
        # attempting to log in
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(request, user)
            return redirect('top20')
        else:
            return render(request,
                          'users/login.html',
                          {'failed': True,
                           'username': username})

    return render(request,
                  'users/login.html')


#

#

#

#
