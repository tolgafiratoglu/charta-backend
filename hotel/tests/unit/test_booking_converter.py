from django.test import TestCase

from hotel.services.reservationservice import ReservationService

from hotel.models.bookingmodel import Booking
from hotel.models.reservationmodel import Reservation

class BookingToReservationTestCase(TestCase):

    def test_booking_to_reservation(self):
        booking_to_convert = Booking(1, 1, '2020-01-01 00:00', '2020-01-03 00:00', 1)
        expected_reservation = Reservation(1, 1, 1, '2020-01-01 00:00', '2020-01-03 00:00')
        converted_reservation = ReservationService.convertBookingToReservation(booking_to_convert)
        # Assert that expected reservation is equal to converted one:
        self.assertEqual(converted_reservation, expected_reservation)