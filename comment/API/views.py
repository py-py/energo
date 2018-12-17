from rest_framework import generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from comment.API.serializers import CommentSerializer
from comment.models import Comment
from .authentication import *

__all__ = ('CommentHtmlView', )


class CommentHtmlView(generics.GenericAPIView):

    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    renderer_classes = (TemplateHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        try:
            url = request.GET['url']
        except KeyError as exc:
            raise exc
        data = {
            'comments': Comment.objects.all().filter(url=url).order_by('-id'),
            'url': url
        }
        return Response(data=data, template_name='comment/modal.html')

    def post(self, request, *args, **kwargs):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            comment = Comment(**serializer.validated_data)
            comment.save()
            return Response(data={'comments': [comment]}, template_name='comment/comment_single.html')
        raise Exception(serializer.errors)

