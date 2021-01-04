from django.http import HttpResponse, HttpResponseBadRequest

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework import generics

from hotel.models.bookingmodel import Booking
from hotel.serializers.bookingserializer import BookingRetrieveSerializer
from hotel.services.bookingservice import BookingService
from hotel.services.visitorservice import VisitorService

from rest_framework.decorators import action

from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer

class BookingView(APIView):
    # Permission Classes:
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer]

    def create(self, request, format=None):
        room = request.data.room
        start_date = request.data.start_date
        end_date = request.data.end_date
        visitor_firstname = request.data.visitor_firstname
        visitor_lastname = request.data.visitor_lastname
        visitor_email = request.data.visitor_email
        visitor_gsm = request.data.visitor_gsm
        # Check previous bookings to see if room and dates are available
        is_room_available = BookingService.is_room_available(room, start_date, end_date)
        if is_room_available == True:
            # Checks the visitor name and creates if not exists:
            visitor_id = VisitorService.get_visitor(visitor_firstname, visitor_lastname, visitor_gsm, visitor_email)
            # If all fine, save the booking:
            if visitor_id > 0:
                BookingService.create();
        else:
            return Response({})