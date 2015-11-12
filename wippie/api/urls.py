__author__ = 'prawit.chaivong'

from rest_framework import routers

# Viewsets
from .viewsets import HolidayViewSet
from .viewsets import TSUserViewSet

router = routers.SimpleRouter()
router.register(r'holiday', HolidayViewSet)
router.register(r'user', TSUserViewSet)

urlpatterns = router.urls
