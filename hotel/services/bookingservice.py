from rest_framework.views import APIView
from hotel.models.bookingmodel import Booking
from hotel.serializers.bookingserializer import BookingSaveSerializer

from django.db.models import Q

class BookingService():

    def is_room_available(room, start_date, end_date):
        query_settle_date = Q(Q(settle_date__gte=start_date) & Q(settle_date__lte=end_date))
        query_leave_date = Q(Q(leave_date__gte=start_date) & Q(leave_date__lte=end_date))
        query_between_date = Q(Q(settle_date__lte=start_date) & Q(leave_date__gte=end_date))
        query_settle_leave = Q(Q(room=room) & Q(query_settle_date | query_leave_date | query_between_date))
        count_matched = Booking.objects.filter(query_settle_leave).count()
        return True if count_matched == 0 else False

    def create(booked_by, room, settle_date, leave_date):
        serializer = BookingSaveSerializer(data={"booked_by":booked_by, "room":room, "settle_date":settle_date, "leave_date":leave_date})
        if serializer.is_valid():
            booking = serializer.save()
            return booking.pk
        else:
            return False   