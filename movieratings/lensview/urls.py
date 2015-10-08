from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^movies/top_20$', views.top_20),
    url(r'^movies/(?P<movie_id>\d+)$', views.show_movie, name='rater_detail'),
    url(r'^raters/(?P<rater_id>\d+)$', views.show_rater, name='movie_detail'),
]
