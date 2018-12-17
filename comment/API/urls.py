from django.urls import path
from rest_framework import routers
from .viewsets import *
from .views import *

router = routers.SimpleRouter()
router.register(r'comments', CommentViewSet)
urls = router.urls

urlpatterns = [
    path('comments/html/', CommentHtmlView.as_view(), name='comment-html')
] + urls
