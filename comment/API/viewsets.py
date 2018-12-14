from rest_framework import viewsets, mixins

from comment.models import Comment
from .serializers import *

__all__ = ('CommentViewSet',)


class CommentViewSet(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):

    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def get_queryset(self):
        queryset = Comment.objects.all()
        try:
            url = self.request.GET['url']
        except KeyError as exc:
            pass
        else:
            queryset = queryset.filter(url=url)
        return queryset
