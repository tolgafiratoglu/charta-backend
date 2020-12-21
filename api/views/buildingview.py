from django.http import HttpResponse, HttpResponseBadRequest

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework import generics

from api.models.buildingmodel import Building
from api.serializers.buildingserializer import BuildingListSerializer

from rest_framework.decorators import action

import json

class BuildingListView(generics.ListAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingListSerializer
    permission_classes = (IsAuthenticated, )

class BuildingRetrieveView(generics.RetrieveAPIView):
    #lookup_field = 'id'
    queryset = Building.objects.all()
    serializer_class = BuildingListSerializer
    permission_classes = (IsAuthenticated, )    