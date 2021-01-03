from rest_framework import serializers
from hotel.models.bookingmodel import Booking

class BookingSaveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = ('booked_by', 'room', 'settle_date', 'leave_date')