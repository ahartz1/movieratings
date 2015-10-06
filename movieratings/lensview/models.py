from django.db import models


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
    rater = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)
    stars = models.IntegerField()

    def __str__(self):
        return 'id={}, rater={}, stars={}, title={}'.format(
            self.id, self.rater, self.stars, self.movie)
