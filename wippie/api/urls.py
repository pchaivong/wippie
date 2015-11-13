__author__ = 'prawit.chaivong'

from rest_framework import routers

# Viewsets
from .viewsets import HolidayViewSet
from .viewsets import TSUserViewSet
from .viewsets import OnCallViewSet
from .viewsets import WipViewSet
from .viewsets import LateViewSet
from .viewsets import LeaveViewSet

router = routers.SimpleRouter()
router.register(r'holiday', HolidayViewSet)
router.register(r'user', TSUserViewSet)
router.register(r'oncall', OnCallViewSet)
router.register(r'wip', WipViewSet)
router.register(r'late', LateViewSet)
router.register(r'leave', LeaveViewSet)

urlpatterns = router.urls
