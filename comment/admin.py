from django.contrib import admin
from django.utils.html import format_html
from mptt.admin import MPTTModelAdmin
from comment.models import Comment

__all__ = ('CommentAdmin', )


class CommentAdmin(MPTTModelAdmin):
    list_display = ('__str__', 'url_link')
    mptt_level_indent = 10

    def url_link(self, obj):
        return format_html('<a href="{href}">{href}</a>'.format(href=obj.url))
    url_link.short_description = 'Link to site'

    def get_form(self, request, obj=None, **kwargs):
        form = super(CommentAdmin, self).get_form(request, obj, **kwargs)
        if obj:
            form.base_fields['parent'].queryset = Comment.objects.filter(url=obj.url)
        return form

admin.site.register(Comment, CommentAdmin)
