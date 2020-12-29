from rest_framework import serializers
from api.models.roommodel import Room

class RoomRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = ('id', 'name', 'code', 'building', 'room_type')