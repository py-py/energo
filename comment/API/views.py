from rest_framework import generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from comment.models import Comment
from .authentication import *

__all__ = ('CommentHtmlView', )


class CommentHtmlView(generics.GenericAPIView):

    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    renderer_classes = (TemplateHTMLRenderer,)

    def post(self, request, *args, **kwargs):
        try:
            url = request.data['url']
        except KeyError as exc:
            raise
        data = {
            'comments': Comment.objects.all().filter(url=url),
            'url': url
        }
        return Response(data=data, template_name='comment/modal.html')
