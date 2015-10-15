from django.core.management.base import BaseCommand
from lensview.models import Movie


class Command(BaseCommand):

    def handle(self, *args, **options):
        for movie in Movie.objects.all():
            try:
                movie.save()
            except:
                continue
