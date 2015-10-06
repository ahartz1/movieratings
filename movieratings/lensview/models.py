from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Rater(models.Model):
    age = models.IntegerField()

    def __str__(self):
        return 'id={}, age={}'.format(self.id, self.age)

class Movie(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return 'id={}, title={}'.format(self.id, self.title)

class Rating(models.Model):
    user = models.ForeignKey(User)
    title = models.ForeignKey(Movie)
    stars = models.IntegerField()

    def __str__(self):
        return 'user={}, stars={}, title={}'.format(self.user,
                                                    self.stars,
                                                    self.title)
