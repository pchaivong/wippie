__author__ = 'prawit.chaivong'
from rest_framework import serializers
from .models import TSUser
from .models import Holiday
# Import your model and create serializer class below


class TSUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TSUser


class HolidaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Holiday


# Create your model serializer class here.
