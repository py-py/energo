from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django import views
from django.urls import reverse

from article.models import Article

__all__ = (
    'ArticleView',
    'ArticleDetailView',
    'ArticleUserView',
)


def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


class ArticleView(views.View):
    def get(self, request):
        data = {
            'articles': Article.objects_active.order_by('-created')
        }
        return render(request, 'article/index.html', context=data)


class ArticleUserView(views.View):
    def get(self, request, id_user):
        try:
            author = User.objects.get(id=id_user)
        except Article.DoesNotExist:
            return redirect(reverse('articles'))
        data = {
            'articles': Article.objects.filter(author=author)
        }
        return render(request, 'article/index.html', context=data)


class ArticleDetailView(views.View):
    def get(self, request, id_article):
        try:
            article = Article.objects.get(id=id_article)
        except Article.DoesNotExist:
            return redirect(reverse('articles'))

        data = {
            'article': article,
            'last_articles': Article.objects.order_by('-created')[:10]
        }
        return render(request, 'article/detail.html', context=data)
