from django.contrib import admin
from article.models import Article

__all__ = ('ArticleModelAdmin', )


class ArticleModelAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'author')

admin.site.register(Article, ArticleModelAdmin)
