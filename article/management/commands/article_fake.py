from random import randint
from faker import Faker

from article.models import Article
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Generate fake articles'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, default=10)

    def handle(self, *args, **options):
        count = options['count']
        fake = Faker()
        fake.text(randint(100, 1000))
        articles = [Article(text=fake.text(randint(100, 1000))) for _ in range(count)]
        Article.objects.bulk_create(articles)

        self.stdout.write(self.style.SUCCESS('Successfully created {} articles.'.format(count)))