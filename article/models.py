from django.db import models
from django.utils.translation import gettext as _

__all__ = ('Article',)


class ArticleManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class Article(models.Model):
    title = models.CharField(verbose_name=_('Title'), max_length=255)
    text = models.TextField(verbose_name=_('Text'))
    created = models.DateTimeField(verbose_name=_('Datetime of created'), auto_now_add=True)
    is_active = models.BooleanField(verbose_name=_('Is Active?'), default=True)
    author = models.ForeignKey('auth.User', verbose_name=_('Author'), on_delete=models.CASCADE, related_name='articles')

    objects = models.Manager()
    objects_active = ArticleManager()

    @property
    def short_text(self):
        LENGHT = 400
        return self.text[:LENGHT] + '...' if len(self.text) >= LENGHT else self.text

    def __str__(self):
        return '{}(id:{})'.format(self.__class__.__name__, self.id, )
