from django.core.management.base import BaseCommand
from datetime import datetime
import csv
import json


class Command(BaseCommand):
    def handle(self, *args, **options):

        # Need to open ml-1m.users.dat with csv
        # Then create a json from it
        user_data = []

        with open('ml-1m/users.dat') as f:
            reader = csv.DictReader([line.replace('::', '\t') for line in f],
                                    fieldnames=['UserID',
                                                'Gender',
                                                'Age',
                                                'Occupation',
                                                'Zip-code'],
                                    delimiter='\t')
            for row in reader:
                user = {
                    'pk': int(row['UserID']),
                    'model': 'lensview.Rater',
                    'fields': {
                        'age': int(row['Age']),
                        'gender': row['Gender'],
                        'occupation': row['Occupation'],
                        'zipcode': row['Zip-code'],
                    },
                }
                user_data.append(user)

        with open('lensview/fixtures/users.json', 'w') as f:
            f.write(json.dumps(user_data))


        # Need to open ml-1m.users.dat with csv
        # Then create a json from it
        movie_data = []

        with open('ml-1m/movies.dat', encoding='windows-1252') as f:
            reader = csv.DictReader([line.replace('::', '\t') for line in f],
                                    fieldnames=['MovieID',
                                                'Title',
                                                'Genres',
                                                ],
                                    delimiter='\t')
            for row in reader:
                movie = {
                    'pk': int(row['MovieID']),
                    'model': 'lensview.Movie',
                    'fields': {
                        'title': row['Title'],
                        'genres': row['Genres'],
                    },
                }
                movie_data.append(movie)

        with open('lensview/fixtures/movies.json', 'w') as f:
            f.write(json.dumps(movie_data))


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
                        'rater': int(row['UserID']),
                        'movie': int(row['MovieID']),
                        'stars': int(row['Rating']),
                        'timestamp': str(datetime.utcfromtimestamp(
                            int(row['Timestamp']))),
                    },
                }
                rating_data.append(rating)

        with open('lensview/fixtures/ratings.json', 'w') as f:
            f.write(json.dumps(rating_data))
