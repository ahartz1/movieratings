from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.db.models import Avg, Count
from django.shortcuts import redirect, render, get_object_or_404
from datetime import datetime
from .forms import UserForm, RaterForm, RatingForm
from .models import Rater, Movie, Rating

# Create your views here.


def movie_detail(request, movie_id):
    if request.method == 'POST' and request.user.is_authenticated():
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.rater = request.user.rater
            rating.movie = Movie.objects.get(pk=movie_id)
            rating.timestamp = datetime.now()
            rating.save()
            return redirect('movie_detail', rating.movie.pk)
        else:
            messages.add_message(request,
                                 messages.ERROR,
                                 'Star rating must be between 1 and 5')
    movie = get_object_or_404(Movie, pk=movie_id)
    ratings = movie.rating_set.all()
    user_stars = None
    if request.user.is_authenticated():
        try:
            user_stars = request.user.rater.rating_set.filter(
                movie_id=movie_id)[0].stars
            return render(request,
                          'lensview/movie_detail.html',
                          {'movie': movie,
                           'ratings': ratings,
                           'user_stars': user_stars})
        except:
            form = RatingForm()
            return render(request,
                          'lensview/movie_detail.html',
                          {'movie': movie,
                           'ratings': ratings,
                           'user_stars': user_stars,
                           'form': form})
    else:
        return render(request,
                      'lensview/movie_detail.html',
                      {'movie': movie,
                       'ratings': ratings,
                       'user_stars': user_stars})


def user_detail(request, rater_id):
    rater = get_object_or_404(Rater, pk=rater_id)
    ratings = rater.rating_set.all().order_by('-stars')
    return render(request,
                  'lensview/user_detail.html',
                  {'rater': rater,
                   'ratings': ratings})


@login_required
def edit_rating(request, rater_id, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    # TODO: Figure out why the below doesn't work
    # if request.user.rater.pk != rater_id:
    #     messages.add_message(request, messages.ERROR,
    #                          'You must be logged in to edit')
    #     return redirect('user_detail', rater_id)

    try:
        rating = Rating.objects.all().filter(rater=request.user.rater,
                                             movie=movie)[0]
    except:
        messages.add_messages(request, messages.ERROR,
                              'No rating exists to change')
        return redirect('user_detail', request.user.rater.pk)

    if request.method == 'GET':
        form = RatingForm(instance=rating)
    elif request.method == 'POST':
        form = RatingForm(instance=rating, data=request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.rater = request.user.rater
            rating.movie = movie
            rating.timestamp = datetime.now()
            rating.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Updated rating for {}'.format(movie))
    return render(request,
                  'lensview/edit_rating.html',
                  {'movie': movie,
                   'rating': rating,
                   'form': form})


@login_required
def delete_rating(request, rater_id, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    try:
        Rating.objects.all().filter(rater=request.user.rater,
                                    movie=movie).delete()

    except:
        messages.add_messages(request, messages.ERROR,
                              'No rating exists to delete')
    return redirect('user_detail', request.user.rater.pk)


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
                  {'top_movies': top_movies,
                   'top_type': 'Average Rating'})


def top_20_by_num_ratings(request):
    most_rated = Movie.objects.annotate(num_raters=Count('rating')) \
        .annotate(avg_rating=Avg('rating__stars')).order_by('-num_raters')[:20]
    return render(request,
                  'lensview/top_20.html',
                  {'top_movies': most_rated,
                   'top_type': 'Number of Raters'})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            # ratings = user.rater.rating_set.all().order_by('-stars')
            return redirect(reverse('user_detail', args=[user.rater.pk]))
        else:
            return render(request,
                          'lensview/user_login.html',
                          {'error_message': "ERROR LOGGING IN!",
                           'username': username})
    else:
        return render(request, 'lensview/user_login.html')


def user_register(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        rater_form = RaterForm(request.POST)

        if user_form.is_valid() and rater_form.is_valid():
            user = user_form.save()
            password = user_form['password']
            user.set_password(password)
            user.save()

            rater = rater_form.save(commit=False)
            rater.user = user

            rater.save()

            user = authenticate(username=user.username, password=password)
            login(request, user)
            return redirect('top_20')
    else:
        user_form = UserForm()
        rater_form = RaterForm()
    return render(request,
                  'lensview/user_register.html',
                  {'user_form': user_form,
                   'rater_form': rater_form})


def user_logout(request):
    if request.user.is_authenticated():
        user_name = request.user.username
        logout(request)
        return render(request,
                      'lensview/user_logout.html',
                      {'user_name': user_name})
    else:
        return redirect('/')
