from rest_framework.views import APIView
from hotel.models.bookingmodel import Booking
from hotel.models.visitormodel import Visitor

from hotel.serializers.bookingserializer import BookingSaveSerializer

from hotel.documents.booking import BookingDocument

from django.db.models import Q

class BookingService():

    @classmethod
    def is_room_available(self, room, start_date, end_date):
        query_settle_date = Q(Q(settle_date__gte=start_date) & Q(settle_date__lte=end_date))
        query_leave_date = Q(Q(leave_date__gte=start_date) & Q(leave_date__lte=end_date))
        query_between_date = Q(Q(settle_date__lte=start_date) & Q(leave_date__gte=end_date))
        query_settle_leave = Q(Q(room=room) & Q(query_settle_date | query_leave_date | query_between_date))
        count_matched = Booking.objects.filter(query_settle_leave).count()
        return True if count_matched == 0 else False

    @classmethod
    def createESDocument(self, id, booked_by, room, settle_date, leave_date):
        visitor_obj = Visitor.objects.filter(id=booked_by).first()
        document = BookingDocument(meta={'id': id})
        document.visior_id = booked_by
        document.visitor_name = visitor_obj.firstname + ' ' + visitor_obj.lastname
        document.settle_date = settle_date
        document.leave_date = leave_date
        document.room = room
        return document.save()

    @classmethod
    def create(self, booked_by, room, settle_date, leave_date, number_of_visitors):
        serializer = BookingSaveSerializer(data={"booked_by":booked_by, "room":room, "settle_date":settle_date, "leave_date":leave_date, "number_of_visitors": number_of_visitors})
        if serializer.is_valid():
            booking = serializer.save()
            # Document in elasticsearch:
            self.createESDocument(booking.pk, booked_by, room, settle_date, leave_date)
            return booking.pk
        else:
            return False   