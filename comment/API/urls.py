from rest_framework import routers
from .viewsets import *

router = routers.SimpleRouter()
router.register(r'comments', CommentViewSet)
urls = router.urls

urlpatterns = urls
