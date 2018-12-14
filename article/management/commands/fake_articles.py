from random import randint

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from faker import Faker

from article.models import Article


class Command(BaseCommand):
    help = 'Generate fake articles'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, nargs='?',  default=4)

    def handle(self, *args, **options):
        count = options['count']
        fake = Faker()

        articles = []
        for user in User.objects.exclude(is_superuser=True):
            articles += [Article(
                text=fake.text(randint(1000, 5000)),
                title=fake.text(40),
                author=user,
            ) for _ in range(count)]

        Article.objects.bulk_create(articles)
        self.stdout.write(self.style.SUCCESS('Successfully created {} articles.'.format(len(articles))))