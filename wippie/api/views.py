from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import TSUser
from .models import OnCall
from .models import Late
from .models import Leave
from .serializers import OnCallSerializer
from .serializers import LateSerializer
from .serializers import LeaveSerializer
# Create your views here.

class OnCallList(generics.ListCreateAPIView):
    model = OnCall
    serializer_class = OnCallSerializer
    filter_field = ('date')

    def post(self, request, format=None):
        serializer = OnCallSerializer(data={
            "date":request.DATA.get("date"),
            "shift_day":request.TSUser.email,
            "shift_night":request.TSUser.email,
            "queue_mananger":request.TSUser.email,
        })
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LateList(generics.ListCreateAPIView):
    model = Late
    serializer_class = LateSerializer
    filter_field = ('date_id')

    def post(self, request, format=None):
        serializer = LateSerializer(data={
            "date_id":request.DATA.get("date_id"),
            "user_id":request.TSUser.email,
        })
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LeaveList(generics.ListCreateAPIView):
    model = Leave
    serializer_class = LeaveSerializer
    filter_field = ('date_id')

    def post(self, request, format=None):
        serializer = LeaveSerializer(data={
            "date_id":request.DATA.get("date_id"),
            "user_id":request.TSUser.email,
            "duration":request.DATA.get("duration")
        })
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
