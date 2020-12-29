from rest_framework import serializers
from hotel.models.buildingmodel import Building

class BuildingRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Building
        fields = ('id', 'name', 'code')