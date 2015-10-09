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
        return self.pk


class Movie(models.Model):
    title = models.CharField(max_length=255)
    genres = models.CharField(max_length=255)

    def __str__(self):
        return self.pk


class Rating(models.Model):
    rater = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)
    stars = models.SmallIntegerField()

    def __str__(self):
        return '@{}: {}\u2505 -> {}'.format(
            self.rater, self.stars, self.movie.title)


def ml_users_to_json():
    import csv
    import json

    # Need to open ml-1m.users.dat with csv
    # Then create a json from it
    user_data = []

    with open('ml-1m/users.dat') as f:
        reader = csv.DictReader([line.replace('::', '\t') for line in f],
                                fieldnames=['UserID',
                                            'Age',
                                            'Gender',
                                            'Occupation',
                                            'Zip-code'],
                                delimiter='\t')
        for row in reader:
            user = {
                'pk': row['UserID'],
                'model': 'lensview.Rater',
                'fields': {
                    'age': row['Age'],
                    'gender': row['Gender'],
                    'occupation': row['Occupation'],
                    'zipcode': row['Zip-code'],
                },
            }
            user_data.append(user)

    with open('lensview/fixtures/users.json', 'w') as f:
        f.write(json.dumps(user_data))


def ml_movies_to_json():
    import csv
    import json

    # Need to open ml-1m.users.dat with csv
    # Then create a json from it
    movie_data = []

    with open('ml-1m/movies.dat') as f:
        reader = csv.DictReader([line.replace('::', '\t') for line in f],
                                fieldnames=['MovieID',
                                            'Title',
                                            'Genres',
                                            ],
                                delimiter='\t')
        for row in reader:
            movie = {
                'pk': row['MovieID'],
                'model': 'lensview.Movie',
                'fields': {
                    'title': row['Title'],
                    'genres': row['Genres'],
                },
            }
            movie_data.append(movie)

    with open('lensview/fixtures/movies.json', 'w') as f:
        f.write(json.dumps(movie_data))


def ml_ratings_to_json():
    import csv
    import json

    # Need to open ml-1m.users.dat with csv
    # Then create a json from it
    rating_data = []

    with open('ml-1m/ratings.dat') as f:
        reader = csv.DictReader([line.replace('::', '\t') for line in f],
                                fieldnames=['UserID',
                                            'MovieID',
                                            'Rating',
                                            'Timestamp',
                                            ],
                                delimiter='\t')
        for row in reader:
            rating = {
                'model': 'lensview.Rating',
                'fields': {
                    'rater': row['UserID'],
                    'movie': row['MovieID'],
                    'stars': row['Rating'],
                },
            }
            rating_data.append(rating)

    with open('lensview/fixtures/ratings.json', 'w') as f:
        f.write(json.dumps(rating_data))

def ml_all_to_json():
    ml_users_to_json()
    ml_movies_to_json()
    ml_ratings_to_json()
