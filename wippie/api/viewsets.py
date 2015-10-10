__author__ = 'prawit.chaivong'
from rest_framework import viewsets
from .serializers import HolidaySerializer
from .serializers import TSUserSerializer
from .models import Holiday
from .models import TSUser


class HolidayViewSet(viewsets.ModelViewSet):
    queryset = Holiday.objects.all()
    serializer_class = HolidaySerializer


class TSUserViewSet(viewsets.ModelViewSet):
    queryset = TSUser.objects.all()
    serializer_class = TSUserSerializer