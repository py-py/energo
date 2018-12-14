import os

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from dotenv import load_dotenv


class Command(BaseCommand):
    help = 'Generate a superuser'

    def handle(self, *args, **options):
        load_dotenv()
        username = os.getenv('SUPERUSER_USERNAME')
        password = os.getenv('SUPERUSER_PASSWORD')
        email = os.getenv('SUPERUSER_EMAIL')

        if username and password and email:
            superuser = User.objects.create_superuser(
                username=username,
                password=password,
                email=email
            )
            self.stdout.write(self.style.SUCCESS('Successfully created superuser: {}.'.format(superuser)))
