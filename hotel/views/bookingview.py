from django.http import HttpResponse, HttpResponseBadRequest

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework import generics

from hotel.models.bookingmodel import Booking
from hotel.serializers.bookingserializer import BookingRetrieveSerializer
from hotel.services.bookingservice import BookService

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
        # Check previous bookings to see if room and dates are available
        is_room_available = BookService.is_room_available(room, start_date, end_date)
        if is_room_available == True:
            # Checks the visitor name and creates if not exists:
        
            # If all fine, save the booking:
        else:
            return Response({})