from django.utils.translation import gettext as _
from rest_framework import serializers
from comment.models import Comment

__all__ = ('CommentSerializer', )


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'text', 'url')
        extra_kwargs = {'url': {'write_only': True}}
