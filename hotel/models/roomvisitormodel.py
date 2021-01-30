from django.db import models
from hotel.models.roommodel import Room
from hotel.models.visitormodel import Visitor


class RoomVisitor(models.Model):
    managed = True
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, default=None, null=True, blank=True)
    visitor = models.ForeignKey(Visitor, on_delete=models.SET_NULL, default=None, null=True, blank=True)
    class Meta:
        db_table = "charta_room_visitor"