from django.db import models
from api.models.visitormodel import Visitor
from api.models.roommodel import Room


class Booking(models.Model):
    managed = True
    name = models.CharField(max_length=255, unique=True, null=False, blank=False)
    booker = models.ForeignKey(Visitor, on_delete=models.SET_NULL, default=None, null=True, blank=True)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, default=None, null=True, blank=True)
    settle_date = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    leave_date = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = "charta_booking"