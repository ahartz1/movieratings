from django.contrib.auth.models import User
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
    zipcode = models.CharField(max_length=5)
    user = models.OneToOneField(User, null=True)

    def __str__(self):
        return self.pk


class Movie(models.Model):
    title = models.CharField(max_length=255)
    genres = models.CharField(max_length=255)

    def __str__(self):
        return self.pk


class Rating(models.Model):
    rater = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)
    stars = models.SmallIntegerField(choices=[(1, '1\u2505'),
                                              (2, '2\u2505'),
                                              (3, '3\u2505'),
                                              (4, '4\u2505'),
                                              (5, '5\u2505'),
                                              ])

    def __str__(self):
        return '@{}: {}\u2505 -> {}'.format(
            self.rater, self.stars, self.movie.title)

def make_raters_users():







#
