from django.db import models
from hotel.models.visitormodel import Visitor
from hotel.models.roommodel import Room
from hotel.models.bookingmodel import Booking


class Reservation(models.Model):
    managed = True
    reserved_by = models.ForeignKey(Visitor, on_delete=models.SET_NULL, default=None, null=True, blank=False)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, default=None, null=True, blank=False)
    booking = models.ForeignKey(Booking, on_delete=models.SET_NULL, default=None, null=True, blank=True)
    settle_date = models.DateTimeField(auto_now_add=False, null=False, blank=False)
    leave_date = models.DateTimeField(auto_now_add=False, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)
    class Meta:
        db_table = "charta_reservation"