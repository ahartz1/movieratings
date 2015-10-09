from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^movies/(?P<movie_id>\d+)$', views.show_movie, name='movie_detail'),
    url(r'^raters/(?P<rater_id>\d+)$', views.show_rater, name='rater_detail'),
    # url(r'^users/(?P<user_id>\d+)$', views.show_rater, name='user_detail'),
    url(r'^user/(?P<username>\S+)$', views.show_user_by_username),
    url(r'', views.top_20, name='top20')
]
