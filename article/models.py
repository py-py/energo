from django.db import models
from django.utils.translation import gettext as _

__all__ = ('Article', )


class Article(models.Model):
    text = models.TextField()
    created = models.DateTimeField(verbose_name=_('Datetime of created'), auto_created=True)
    is_active = models.BooleanField(verbose_name=_('State'), default=True)
    owner = models.ForeignKey('auth.User', verbose_name=_('Owner'), on_delete=models.CASCADE, related_name='articles')

    def __str__(self):
        return '{}(id:{}, owner:{})'.format(self.__class__.__name__, self.id, self.owner.username)
