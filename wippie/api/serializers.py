__author__ = 'prawit.chaivong'
from rest_framework import serializers
from .models import TSUser
from .models import Holiday


class TSUserSerializer(serializers.ModelSerializer):
    fullname = serializers.CharField(source='get_full_name', read_only=True)

    class Meta:
        model = TSUser
        exclude = ('password', 'is_admin', 'is_active', 'last_login')


class HolidaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Holiday
        exclude = ('id',)
