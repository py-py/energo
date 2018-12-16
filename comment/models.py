from django.db import models
from django.utils.translation import gettext as _
from mptt.models import MPTTModel, TreeForeignKey

__all__ = ('Comment', )


class Comment(MPTTModel):
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    # application_id = models.PositiveIntegerField(verbose_name=_('Application ID'))
    # article_id = models.PositiveIntegerField(verbose_name=_('Article ID'))
    # user_id = models.PositiveIntegerField(verbose_name=_('User ID'))
    url = models.URLField(verbose_name=_('Ссылка'), null=False, blank=False)
    text = models.TextField(verbose_name=_('Комментарий'))

    class MPTTMeta:
        pass

    def __str__(self):
        short_text = self.text[:20] + '...'
        return '{}("{}")'.format(self.__class__.__name__, short_text)
