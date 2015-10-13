from django.core.management.base import BaseCommand
from lensview.models import Rater
from django.contrib.auth.models import User
from faker import Faker
from random import choice


class Command(BaseCommand):

    def handle(self, *args, **options):
        fake = Faker()

        for rater in Rater.objects.all():
            if rater.user is None:
                while True:
                    fake_username = fake.user_name() + \
                        choice(list('0123456789'))
                    try:
                        rater.user = User.objects.create_user(fake_username,
                                                              fake.email(),
                                                              'password')
                        rater.save()
                        break
                    except:
                        continue
