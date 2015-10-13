from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
# Create your models here.


class Rater(models.Model):
    MALE = 'M'
    FEMALE = 'F'

    GENDER = (
        (MALE, 'Male'),
        (FEMALE, 'Female')
    )

    gender = models.CharField(max_length=1, choices=GENDER)
    age = models.SmallIntegerField()
    occupation = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=10)
    user = models.OneToOneField(User, null=True)

    def __str__(self):
        return str(self.pk)


class Movie(models.Model):
    title = models.CharField(max_length=255)
    genres = models.CharField(max_length=255)

    def __str__(self):
        return str(self.pk)

    def average_rating(self):
        return self.rating_set.aggregate(models.Avg('stars'))['stars__avg']


def is_valid_stars(value):
    if not (1 <= value <= 5):
        raise ValidationError('Star value must be between 1 and 5')


class Rating(models.Model):
    rater = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)
    stars = models.SmallIntegerField(choices=[(1, u'\u2605'),
                                              (2, u'\u2605' * 2),
                                              (3, u'\u2605' * 3),
                                              (4, u'\u2605' * 4),
                                              (5, u'\u2605' * 5)],
                                     validators=[is_valid_stars])
    timestamp = models.DateTimeField()
    review = models.TextField(max_length=511, null=True, blank=True)

    def __str__(self):
        return '@{}: {}\u2605 -> {}'.format(
            self.rater, self.stars, self.movie.title)

    def rater_username(self):
        return self.rater.user.username

    def movie_title(self):
        return self.movie.title
