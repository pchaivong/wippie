__author__ = 'prawit.chaivong'

from rest_framework import routers

# Viewsets
from .viewsets import HolidayViewSet

router = routers.SimpleRouter()
router.register(r'holiday', HolidayViewSet)
# add your route here.
# router.register(r'late', LateViewSet)



# don't touch it
urlpatterns = router.urls
