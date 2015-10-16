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

    AGE = (
        (1, "Under 18"),
        (18, "18–24"),
        (25, "25–34"),
        (35, "35–44"),
        (45, "45–49"),
        (50, "50–55"),
        (56, "56+"),
    )

    OCCUPATION = (
        (0, '"other" or not specified'),
        (1, "academic/educator"),
        (2, "artist"),
        (3, "clerical/admin"),
        (4, "college/grad student"),
        (5, "customer service"),
        (6, "doctor/health care"),
        (7, "executive/managerial"),
        (8, "farmer"),
        (9, "homemaker"),
        (10, "K–12 student"),
        (11, "lawyer"),
        (12, "programmer"),
        (13, "retired"),
        (14, "sales/marketing"),
        (15, "scientist"),
        (16, "self-employed"),
        (17, "technician/engineer"),
        (18, "tradesman/craftsman"),
        (19, "unemployed"),
        (20, "writer"),
    )

    gender = models.CharField(max_length=1, choices=GENDER)
    age = models.SmallIntegerField(choices=AGE)
    occupation = models.SmallIntegerField(choices=OCCUPATION)
    zipcode = models.CharField(max_length=10)
    user = models.OneToOneField(User, null=True)

    def __str__(self):
        return str(self.pk)


class Movie(models.Model):
    title = models.CharField(max_length=255)
    genres = models.CharField(max_length=255)
    avg_rating = models.FloatField(null=True, blank=True)
    num_raters = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.pk)

    def average_rating(self):
        return self.rating_set.aggregate(models.Avg('stars'))['stars__avg']

    def save(self):
        super(Movie, self).save()
        self.avg_rating = self.average_rating()
        self.num_raters = self.rating_set.all().count()
        super(Movie, self).save()


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

    def save(self):
        super(Rating, self).save()
        Movie.objects.get(pk=self.movie_id).save()

    def rater_username(self):
        return self.rater.user.username

    def movie_title(self):
        return self.movie.title
