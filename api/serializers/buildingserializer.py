from rest_framework import serializers
from api.models.buildingmodel import Building

class BuildingListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Building
        fields = ('id', 'name', 'code')