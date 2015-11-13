__author__ = 'prawit.chaivong'
from rest_framework import viewsets
from .serializers import HolidaySerializer
from .serializers import TSUserSerializer
from .serializers import OnCallSerializer
from .serializers import WipSerializer
from .serializers import LateSerializer
from .serializers import LeaveSerializer
from .models import Holiday
from .models import TSUser
from .models import OnCall
from .models import Wip
from .models import Late
from .models import Leave


class HolidayViewSet(viewsets.ModelViewSet):
    queryset = Holiday.objects.all()
    serializer_class = HolidaySerializer


class TSUserViewSet(viewsets.ModelViewSet):
    queryset = TSUser.objects.all()
    serializer_class = TSUserSerializer


class OnCallViewSet(viewsets.ModelViewSet):
    queryset = OnCall.objects.all()
    serializer_class = OnCallSerializer


class WipViewSet(viewsets.ModelViewSet):
    queryset = Wip.objects.all()
    serializer_class = WipSerializer


class LateViewSet(viewsets.ModelViewSet):
    queryset = Late.objects.all()
    serializer_class = LateSerializer


class LeaveViewSet(viewsets.ModelViewSet):
    queryset = Leave.objects.all()
    serializer_class = LeaveSerializer
