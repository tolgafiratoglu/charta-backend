from rest_framework import serializers
from hotel.models.reservationmodel import Reservation

class ReservationSaveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reservation
        fields = ('reserved_by', 'room', 'settle_date', 'leave_date', 'booking')


class ReservationRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reservation
        fields = ('id', 'booked_by', 'room', 'settle_date', 'leave_date', 'booking')