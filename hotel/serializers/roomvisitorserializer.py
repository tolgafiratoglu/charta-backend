from rest_framework import serializers
from hotel.models.roomtypevisitor import RoomVisitor

class RoomVisitorSerializer(serializers.ModelSerializer):

    class Meta:
        model = RoomVisitor
        fields = ('room', 'visitor')