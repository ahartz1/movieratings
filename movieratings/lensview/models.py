from django.db import models


# Create your models here.
class Rater(models.Model):
    age = models.IntegerField()

    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'
    X = 'X'

    # Maps choice to "readable" display for admin input
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
        (X, 'Did not answer'),
    )

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return str(self.id)

    def movie_ratings(self):
        return self.rating_set.all()


class Movie(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    def average_rating(self):
        return self.rating_set.aggregate(models.Avg('stars'))['stars__avg']


class Rating(models.Model):
    rater = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)
    stars = models.PositiveSmallIntegerField()

    def __str__(self):
        return '@{} {}* -> {})'.format(
            self.rater, self.stars, self.movie)
