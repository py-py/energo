from django.urls import path, include
from article.views import *

urlpatterns = [
    path('articles/', ArticleView.as_view(), name='articles'),
    path('articles/<int:id_article>/', ArticleDetailView.as_view(), name='article')
]
