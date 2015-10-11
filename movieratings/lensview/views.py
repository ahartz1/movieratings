from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.db.models import Avg, Count
from django.shortcuts import redirect, render
from .forms import UserForm, RaterForm
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


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            # ratings = user.rater.rating_set.all().order_by('-stars')
            return redirect(reverse('user_detail',
                                    args=[user.rater.pk]))
        else:
            return render(request,
                          'lensview/user_login.html',
                          {'error_message': "ERROR LOGGING IN!",
                           'username': username})
    else:
        return render(request,
                      'lensview/user_login.html')


def user_register(request):
    if request.method == 'POST':
        # form = UserForm(request.POST)
        user_form = UserForm(request.POST)
        rater_form = RaterForm(request.POST)

        # if user_form.is_valid():
        if user_form.is_valid() and rater_form.is_valid():
            user = user_form.save()
            password = user_form['password']
            user.set_password(password)
            user.save()

            # rater_form.cleaned_data['user'] = user
            rater = rater_form.save(commit=False)
            rater.user = user

            # rater = Rater(
            #     user=user,
            # )
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
