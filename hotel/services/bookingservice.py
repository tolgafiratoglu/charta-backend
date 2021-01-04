from rest_framework.views import APIView
from hotel.models.bookingmodel import Booking
from hotel.serializers.bookingserializer import BookingSaveSerializer

class BookingService(APIView):

    def is_room_available(room, start_date, end_date):
        count_matched = Booking.filter(room=room, settle_date__gt=start_date, leave_date__lt=end_date).count()
        return True if count_matched == 0 else False

    def create(booked_by, room, settle_date, leave_date):
        serializer = BookingSaveSerializer(data={booked_by=booked_by, room=room, settle_date=settle_date, leave_date=leave_date})
        if serializer.is_valid():
            serializer.save()
            return serializer.data.id