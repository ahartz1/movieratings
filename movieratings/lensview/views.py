from django.shortcuts import render
# from django.http import HttpResponse
# from .models import Rater, Movie, Rating
from .models import Movie


# Create your views here.
def top_20(request):
    movies = Movie.objects.order_by('-average_rating')[:20]
    return render(request,
                  'lensview/top_20.html',
                  {'movies': movies})
