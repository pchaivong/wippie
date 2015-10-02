__author__ = 'prawit.chaivong'
from rest_framework import viewsets
from .models import Holiday
from .serializers import HolidaySerializer


class HolidayViewSet(viewsets.ModelViewSet):
    queryset = Holiday.objects.all()
    serializer_class = HolidaySerializer

