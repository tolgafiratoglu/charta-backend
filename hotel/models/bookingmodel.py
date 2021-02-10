from django.db import models
from hotel.models.visitormodel import Visitor
from hotel.models.roommodel import Room


class Booking(models.Model):
    managed = True
    booked_by = models.ForeignKey(Visitor, on_delete=models.SET_NULL, default=None, null=True, blank=False)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, default=None, null=True, blank=False)
    settle_date = models.DateTimeField(auto_now_add=False, null=False, blank=False)
    leave_date = models.DateTimeField(auto_now_add=False, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    number_of_visitors = models.IntegerField()
    deleted = models.BooleanField(default=False)

    def __init__(self, booked_by, room, settle_date, leave_date, number_of_visitors):
        self.booked_by = booked_by
        self.room = room
        self.settle_date = settle_date
        self.leave_date = leave_date
        self.number_of_visitors = number_of_visitors

    class Meta:
        db_table = "charta_booking"