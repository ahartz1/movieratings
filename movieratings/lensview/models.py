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
    user = models.OneToOneField(User)

    def __str__(self):
        return self.pk


class Movie(models.Model):
    title = models.CharField(max_length=255)
    genres = models.CharField(max_length=255)

    def __str__(self):
        return self.pk


class Rating(models.Model):
    rater = Rater()
    movie = Movie()
    stars = models.SmallIntegerField()

    def __str__(self):
        return '@{}: {}\u2505 -> {}'.format(
            self.rater, self.stars, self.movie.title)


#

#

#
