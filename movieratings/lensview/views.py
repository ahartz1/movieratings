from django.shortcuts import render
# from django.http import HttpResponse
# from .models import Rater, Movie, Rating
from .models import Movie, Rater


# Create your views here.
def top_20(request):
    # This is just a placeholder until I get the average rating sort to work
    movies = Movie.objects.all()[:20]
    # movies = Movie.objects.all().order_by('-avg_rating')[:20]
    # movies = list(Movie.objects.all())
    # movie_list = [[movie, movie.rating_set.average_rating()]
    #               for movie in movies]
    # # sorted_movie_list = sorted(movie_list,
    #                            key=lambda m: m[1],
    #                            reversed=True
    #                            )[:20]
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
