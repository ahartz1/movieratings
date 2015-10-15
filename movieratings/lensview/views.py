from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.db.models import Avg, Count
# from django.http import Http404
from django.shortcuts import redirect, render, get_object_or_404
from django.views import generic
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
    ratings = movie.rating_set.all().order_by('-timestamp')
    ratings = ratings.prefetch_related('rater__user')
    request, ratings = apply_pagination(request, ratings, 20)
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


# class RaterDetailListView(generic.ListView):
#     model = Rater
#     template_name = 'lensview/rater_detail.html'
#     context_object_name = 'ratings'
#     paginate_by = 20
#
#     def get_queryset(self):
#         self.rater = Rater.objects.get(pk=self.kwargs['pk'])
#         ratings = Rating.objects.order_by('-stars') \
#             .prefetch_related('movie')
#         self.num_rated = len(ratings)
#         return ratings

def rater_detail(request, rater_id):
    rater = get_object_or_404(Rater, pk=rater_id)
    ratings = rater.rating_set.all().order_by('-timestamp')
    ratings = ratings.prefetch_related('movie')
    num_rated = ratings.count()

    request, ratings = apply_pagination(request, ratings, 20)

    return render(request,
                  'lensview/rater_detail.html',
                  {'rater': rater,
                   'num_rated': num_rated,
                   'ratings': ratings})


def apply_pagination(request, set_of_things, num_per_page):
    paginator = Paginator(set_of_things, num_per_page)

    page = request.GET.get('page')
    try:
        set_of_things = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        set_of_things = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        set_of_things = paginator.page(paginator.num_pages)
    return request, set_of_things


@login_required
def edit_rating(request, rater_id, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.user.rater.pk != int(rater_id):
        messages.add_message(request, messages.ERROR,
                             'You must be logged in to edit')
        return redirect('user_detail', rater_id)

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
    if request.user.rater.pk != int(rater_id):
        messages.add_message(request, messages.ERROR,
                             'You must be logged in to delete')
    try:
        Rating.objects.all().filter(rater=request.user.rater,
                                    movie=movie).delete()

    except:
        messages.add_messages(request, messages.ERROR,
                              'No rating exists to delete')
    return redirect('user_detail', request.user.rater.pk)


class TopMoviesByAvgListView(generic.ListView):
    template_name = 'lensview/top_movies.html'
    context_object_name = 'movies'
    paginate_by = 20
    top_type = 'Average Rating'

    def get_queryset(self):
        return Movie.objects.all().filter(
            num_raters__gte=150).order_by('-avg_rating')


class TopMoviesByNumListView(generic.ListView):
    template_name = 'lensview/top_movies.html'
    context_object_name = 'movies'
    paginate_by = 20
    top_type = 'Number of Ratings'

    def get_queryset(self):
        return Movie.objects.all().order_by('-num_raters')


# USER FUNCTIONS: LOGIN, REGISTER, LOGOUT

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
            messages.add_message(request,
                                 messages.SUCCESS,
                                 'Your account was successfully created.')
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
        messages.add_message(request, messages.SUCCESS,
                             "You have successfully logged out")
        return render(request,
                      'lensview/user_logout.html',
                      {'user_name': user_name})
    else:
        return redirect('/')
