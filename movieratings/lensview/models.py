from django.db import models


# Create your models here.
class Rater(models.Model):
    age = models.IntegerField()
    gender = models.CharField(max_length=10)

    def __str__(self):
        return 'Rater(id={}, age={}, gender={})'.format(
            self.id, self.age, self.gender)

    # def movie_ratings(self):
    #     rating_sum = 0
    #     for r in self.rating_set:
    #


class Movie(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return 'Movie(id={}, title={})'.format(
            self.id, self.title)


class Rating(models.Model):
    rater = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)
    stars = models.IntegerField()

    def __str__(self):
        return 'Rating(id={}, rater={}, stars={}, movie={})'.format(
            self.id, self.rater, self.stars, self.movie)
