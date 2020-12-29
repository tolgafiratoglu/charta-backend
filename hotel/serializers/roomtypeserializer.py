from rest_framework import serializers
from hotel.models.roomtypemodel import RoomType

class RoomTypeRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = RoomType
        fields = ('id', 'name')