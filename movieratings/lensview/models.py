from django.db import models


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
        return self.rating_set.aggregate(models.Avg('stars'))['stars__avg']


class Rating(models.Model):
    rater = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)
    stars = models.PositiveSmallIntegerField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return '@{} {}* -> {})'.format(
            self.rater, self.stars, self.movie)


def load_ml_user_data():
    import csv
    import json

    users = []

    with open('ml-1m/users.dat') as f:

        reader = csv.DictReader([line.replace('::', '\t') for line in f],
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

            with open('fixtures/users.json', 'w') as f:
                f.write(json.dumps(users))

        print(json.dumps(users, sort_keys=True, indent=4,
                         separators=(', ', ': ')))


def load_ml_movie_data():
    import csv
    import json

    movies = []

    with open('ml-1m/movies.dat', encoding='windows-1252') as f:

        reader = csv.DictReader([line.replace('::', '\t') for line in f],
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

        print(json.dumps(movies, sort_keys=True, indent=4,
                         separators=(', ', ': ')))

# def load_ml_rating_data():
#     import csv
#     import json
#
#     ratings = []
#
#     with open('ml-1m/movies.dat') as f:
#
#         rating = csv.DictReader([line.replace('::', '\t') for line in f],
#                                 fieldnames='MovieID::Title::Genres'
#                                 .split('::'),
#                                 delimiter='\t')
#
#         for row in reader:
#             movie = {
#                 'fields': {
#                     'title': row['Title'],
#                     'genre': row['Genres'],
#                 },
#                 'model': 'lensview.Movie',
#                 'pk': int(row['MovieID'])
#             }
#
#             movies.append(movie)
#
#             with open('lensview/fixtures/movies.json', 'w') as f:
#                 f.write(json.dumps(movies))
#
#         print(json.dumps(movies, sort_keys=True, indent=4,
#                          separators=(', ', ': ')))
# UserID::MovieID::Rating::Timestamp


#
