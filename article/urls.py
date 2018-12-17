from django.urls import path, include
from article.views import *

urlpatterns = [
    path('', ArticleView.as_view()),
    path('articles/', ArticleView.as_view(), name='articles'),
    path('articles/<int:id_article>/', ArticleDetailView.as_view(), name='article'),

    path('articles/users/<int:id_user>/', ArticleUserView.as_view(), name='articles-user'),
]
