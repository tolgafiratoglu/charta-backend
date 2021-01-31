from django.http import HttpResponse, HttpResponseBadRequest

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework import generics

from hotel.models.reservationmodel import Booking
from hotel.serializers.reservationserializer import ReservationSaveSerializer
from hotel.services.reservationservice import ReservationService
from hotel.services.visitorservice import VisitorService
from hotel.services.bookingservice import BookingService

from rest_framework.decorators import action

from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

class ReservationView(APIView):
    # Permission Classes:
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer]

    def post(self, request, format=None):
        room = int(request.data.get("room", 0))
        start_date = request.data.get("start_date", "")
        end_date = request.data.get("end_date", "")
        visitor_firstname = request.data.get("visitor_firstname", "")
        visitor_lastname = request.data.get("visitor_lastname", "")
        visitor_email = request.data.get("visitor_email", "")
        visitor_gsm = request.data.get("visitor_gsm", "")
        number_of_visitors = request.data.get("number_of_visitors", 1)
        # Check previous bookings to see if room and dates are available
        is_room_available_for_booking = BookingService.is_room_available(room, start_date, end_date)
        is_room_available_for_reservation = ReservationService.is_room_available(room, start_date, end_date)
        if is_room_available_for_booking == True & is_room_available_for_reservation == True:
            # Creates a new visitor row:
            visitor = VisitorService.create(visitor_firstname, visitor_lastname, visitor_gsm, visitor_email)
            # If all fine, save the booking:
            if visitor > 0:
                reservation_id = ReservationService.create(visitor, room, start_date, end_date, number_of_visitors)
                return Response(reservation_id, 200)
            else:
                return Response('Problem during adding the visitor', 400)
        else:
            return Response('Room is not available to be reserved within given date range', 400)