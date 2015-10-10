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
        return str(self.pk)


class Movie(models.Model):
    title = models.CharField(max_length=255)
    genres = models.CharField(max_length=255)

    def __str__(self):
        return str(self.pk)

    def average_rating(self):
        return self.rating_set.aggregate(models.Avg('stars'))['stars__avg']


class Rating(models.Model):
    rater = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)
    stars = models.SmallIntegerField(choices=[(1, u'\u2605'),
                                              (2, u'\u2605' * 2),
                                              (3, u'\u2605' * 3),
                                              (4, u'\u2605' * 4),
                                              (5, u'\u2605' * 5),
                                              ])

    def __str__(self):
        return '@{}: {}\u2605 -> {}'.format(
            self.rater, self.stars, self.movie.title)

    def rater_username(self):
        return self.rater.user.username

    def movie_title(self):
        return self.movie.title


def make_raters_users():
    from faker import Faker
    from random import choice

    fake = Faker()

    for rater in Rater.objects.all():
        if rater.user is None:
            while True:
                fake_username = fake.user_name() + choice(list('0123456789'))
                try:
                    rater.user = User.objects.create_user(fake_username,
                                                          fake.email(),
                                                          'password')
                    rater.save()
                    break
                except:
                    continue
#
