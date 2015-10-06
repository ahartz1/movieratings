from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Rater(models.Model):
    age = models.IntegerField()
    gender = models.CharField(max_length=10)

    def __str__(self):
        return 'id={}, age={}, gender={}'.format(
            self.id, self.age, self.gender)

    # def movie_ratings(self):
    #     return self.movie_set


class Movie(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return 'id={}, title={}'.format(
            self.id, self.title)


class Rating(models.Model):
    user = models.ForeignKey(User)
    title = models.ForeignKey(Movie)
    stars = models.IntegerField()

    def __str__(self):
        return 'user={}, stars={}, title={}'.format(
            self.user, self.stars, self.title)
