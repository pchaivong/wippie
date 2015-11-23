__author__ = 'prawit.chaivong'
from django.utils import six
from rest_framework import serializers
from .models import TSUser
from .models import Holiday
from .models import OnCall
from .models import Wip
from .models import Late
from .models import Leave


class TSUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TSUser
        exclude = ('password', 'last_login',)


class HolidaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Holiday

class OnCallSerializer(serializers.ModelSerializer):
    shift_day = serializers.SlugRelatedField(slug_field='email',queryset=TSUser.objects.all())
    shift_night = serializers.SlugRelatedField(slug_field='email',queryset=TSUser.objects.all())
    queue_manager = serializers.SlugRelatedField(slug_field='email',queryset=TSUser.objects.all())
    class Meta:
        model = OnCall



class WipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wip


class LateSerializer(serializers.ModelSerializer):
    date_id = serializers.SlugRelatedField(slug_field='date',queryset=Wip.objects.all())
    user_id = serializers.SlugRelatedField(slug_field='email',queryset=TSUser.objects.all())
    class Meta:
        model = Late



class LeaveSerializer(serializers.ModelSerializer):
    date_id = serializers.SlugRelatedField(slug_field='date', queryset=Wip.objects.all())
    user_id = serializers.SlugRelatedField(slug_field='email',queryset=TSUser.objects.all())
    class Meta:
        model = Leave
