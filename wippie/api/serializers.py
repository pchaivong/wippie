__author__ = 'prawit.chaivong'
from rest_framework import serializers
from .models import TSUser
from .models import Holiday


class TSUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TSUser
        exclude = ('password', 'last_login',)


class HolidaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Holiday
