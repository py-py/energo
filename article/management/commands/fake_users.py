from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from faker import Faker


class Command(BaseCommand):
    help = 'Generate fake articles'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, nargs='?', default=5)

    def handle(self, *args, **options):
        count = options['count']
        fake = Faker()

        for _ in range(count):
            user = User.objects.create_user(
                username=fake.user_name(),
                password=fake.password(),
                email=fake.email(),
                first_name=fake.first_name(),
                last_name=fake.last_name(),
            )

            self.stdout.write(self.style.SUCCESS('Successfully created {} user.'.format(user.username)))