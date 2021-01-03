from django.db import models
from hotel.models.visitormodel import Visitor
from hotel.models.roommodel import Room


class Booking(models.Model):
    managed = True
    booked_by = models.ForeignKey(Visitor, on_delete=models.SET_NULL, default=None, null=True, blank=True)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, default=None, null=True, blank=True)
    settle_date = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    leave_date = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)
    class Meta:
        db_table = "charta_booking"