from django.http import HttpResponse, HttpResponseBadRequest

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework import generics

from hotel.models.roommodel import Room
from hotel.serializers.roomserializer import RoomRetrieveSerializer

from rest_framework.decorators import action

import json

class RoomListView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomRetrieveSerializer
    permission_classes = (IsAuthenticated, )

class RoomRetrieveView(generics.RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomRetrieveSerializer
    permission_classes = (IsAuthenticated, )    