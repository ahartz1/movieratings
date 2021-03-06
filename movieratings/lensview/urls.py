"""movieratings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from . import views as lv

urlpatterns = [
    url(r'^movies/(?P<movie_id>\d+)$', lv.movie_detail, name='movie_detail'),
    url(r'^users/(?P<rater_id>\d+)$', lv.user_detail, name='user_detail'),
    url(r'^users/(?P<rater_id>\d+)/edit-rating/(?P<movie_id>\d+)$',
        lv.edit_rating, name='edit_rating'),
    url(r'^users/(?P<rater_id>\d+)/delete-rating/(?P<movie_id>\d+)$',
        lv.delete_rating, name='delete_rating'),
    url(r'^top-20/num-ratings$', lv.top_20_by_num_ratings,
        name='top_20_by_num_ratings'),
    # url(r'^top-20/highest-rated$', lv.top_20,
    #     name='top_20_by_num_ratings'),
    url(r'^$', lv.top_20, name='top_20')
]
