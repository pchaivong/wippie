__author__ = 'prawit.chaivong'
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
    shift_day = serializers.PrimaryKeyRelatedField(queryset=TSUser.objects.all())
    shift_night = serializers.PrimaryKeyRelatedField(queryset=TSUser.objects.all())
    queue_manager = serializers.PrimaryKeyRelatedField(queryset=TSUser.objects.all())
    class Meta:
        model = OnCall
        fields = ('date','shift_day','shift_night','queue_manager')


class WipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wip


class LateSerializer(serializers.ModelSerializer):
    date_id = serializers.PrimaryKeyRelatedField(queryset=Wip.objects.all())
    user_id = serializers.PrimaryKeyRelatedField(queryset=TSUser.objects.all())
    class Meta:
        model = Late
        fields = ('date_id','user_id')


class LeaveSerializer(serializers.ModelSerializer):
    date_id = serializers.PrimaryKeyRelatedField(queryset=Wip.objects.all())
    user_id = serializers.PrimaryKeyRelatedField(queryset=TSUser.objects.all())
    class Meta:
        model = Leave
        fields = ('date_id','user_id','duration')