from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from comment.models import Comment

__all__ = ('CommentAdmin', )


class CommentAdmin(MPTTModelAdmin):
    # list_display = ('__str__', 'url')
    mptt_level_indent = 10
    pass

admin.site.register(Comment, CommentAdmin)