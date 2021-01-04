from rest_framework import serializers
from hotel.models.visitormodel import Visitor

class VisitorSaveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Visitor
        fields = ('gsm', 'email', 'firstname', 'lastname')