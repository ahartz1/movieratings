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
    url(r'^movies/(?P<movie_id>\d+)/rate$', lv.rate_movie, name='rate_movie'),
    url(r'^$', lv.top_20, name='top_20')
]
