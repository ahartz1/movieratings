from django.db import models
from django.contrib.auth.models import User
from faker import Faker
from random import choice

# Create your models here.


class Rater(models.Model):
    age = models.PositiveSmallIntegerField()

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
    occupation = models.CharField(max_length=40)
    zipcode = models.CharField(max_length=5)
    user = models.OneToOneField(User, null=True)

    def __str__(self):
        return str(self.id)

    def movie_ratings(self):
        return self.rating_set.all()


class Movie(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    def average_rating(self):
        return self.rating_set.aggregate(
            models.Avg('stars'))['stars__avg']
    avg_rating = property(average_rating)


class Rating(models.Model):
    rater = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)
    stars = models.PositiveSmallIntegerField()

    def __str__(self):
        return '@{} {}\u2605 -> {})'.format(
            self.rater, self.stars, self.movie)


def make_raters_users():
    fake = Faker()
    for rater in Rater.objects.all():
        fake_username = ''
        while True:
            if rater.user_id is None:
                fake_username = fake.user_name() + choice('1234567890'.split())
                try:
                    rater.user = User.objects.create_user(fake_username,
                                                          fake.email(),
                                                          'password')
                    rater.save()
                    break
                except:
                    continue
            else:
                break


def load_ml_user_data():
    import csv
    import json

    users = []

    with open('ml-1m/users.dat') as f:

        reader = csv.DictReader(
            [line.replace('::', '\t') for line in f],
            fieldnames='UserID::Gender::Age::Occupation::'
            'Zip-code'.split('::'),
            delimiter='\t')

        for row in reader:
            user = {
                'fields': {
                    'gender': row['Gender'],
                    'age': row['Age'],
                    'occupation': row['Occupation'],
                    'zipcode': row['Zip-code']
                },
                'model': 'lensview.Rater',
                'pk': int(row['UserID'])
            }

            users.append(user)

        with open('lensview/fixtures/users.json', 'w') as f:
            f.write(json.dumps(users))


def load_ml_movie_data():
    import csv
    import json

    movies = []

    with open('ml-1m/movies.dat', encoding='windows-1252') as f:

        reader = csv.DictReader(
            [line.replace('::', '\t') for line in f],
            fieldnames='MovieID::Title::Genres'
            .split('::'),
            delimiter='\t')

        for row in reader:
            movie = {
                'fields': {
                    'title': row['Title'],
                    'genre': row['Genres'],
                },
                'model': 'lensview.Movie',
                'pk': int(row['MovieID'])
            }

            movies.append(movie)

        with open('lensview/fixtures/movies.json', 'w') as f:
            f.write(json.dumps(movies))


def load_ml_rating_data():
    import csv
    import json

    ratings = []

    with open('ml-1m/ratings.dat') as f:

        reader = csv.DictReader(
            [line.replace('::', '\t') for line in f],
            fieldnames='UserID::MovieID::Rating::Timestamp'
            .split('::'),
            delimiter='\t')

        for row in reader:
            rating = {
                'fields': {
                    'rater': row['UserID'],
                    'movie': row['MovieID'],
                    'stars': row['Rating'],
                },
                'model': 'lensview.Rating',
            }

            ratings.append(rating)

        with open('lensview/fixtures/ratings.json', 'w') as f:
            f.write(json.dumps(ratings))


def load_all_ml_data():
    import csv
    import json
    print('Starting User Data Conversion to JSON.')
    load_ml_user_data()
    print('Starting Movie Data Conversion to JSON.')
    load_ml_movie_data()
    print('Starting Rating Data Conversion to JSON.')
    load_ml_rating_data()

#
