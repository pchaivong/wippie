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
    shift_day = serializers.StringRelatedField()
    shift_night = serializers.StringRelatedField()
    queue_manager = serializers.StringRelatedField()
    class Meta:
        model = OnCall


class WipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wip


class LateSerializer(serializers.ModelSerializer):
    date_id = serializers.StringRelatedField()
    user_id = serializers.StringRelatedField()
    class Meta:
        model = Late
        fields = ('date_id','user_id')


class LeaveSerializer(serializers.ModelSerializer):
    date_id = serializers.StringRelatedField()
    user_id = serializers.StringRelatedField()
    class Meta:
        model = Leave