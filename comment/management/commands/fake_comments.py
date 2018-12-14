from django.core.management import BaseCommand
from django.urls import reverse
from faker import Faker

from article.models import Article
from comment.models import Comment


class Command(BaseCommand):
    help = 'Generate fake comments'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, nargs='?', default=5)

    def handle(self, *args, **options):
        count = options['count']
        fake = Faker()

        articles = Article.objects.all()
        for article in articles:
            url = reverse('article:article', kwargs={'id_article': article.id})
            for _ in range(count):
                comment = Comment(url=url, text=fake.text())
                comment.save()
            self.stdout.write(self.style.SUCCESS('Successfully added {} comments for post: {}.'.format(count, url)))