from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Rater(models.Model):
    user = models.ForeignKey(User)


class Movie(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return '{}'.format(self.title)

class Rating(models.Model):
    user = models.ForeignKey(User)
    title = models.ForeignKey(Movie)
    stars = models.IntegerField()

    def __str__(self):
        return '{}, {}: {}'.format(self.user,
                                   self.stars,
                                   self.title)
