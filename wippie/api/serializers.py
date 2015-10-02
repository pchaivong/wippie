__author__ = 'prawit.chaivong'
from rest_framework import serializers
from .models import UserProfile
from .models import Holiday


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile


class HolidaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Holiday
