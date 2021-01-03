from rest_framework.views import APIView
from hotel.models.bookingmodel import Booking

class BookService(APIView):

    def is_room_available(room, start_date, end_date):
        count_matched = Booking.filter(room=room, settle_date__gt=start_date, leave_date__lt=end_date).count()
        return True if count_matched == 0 else False