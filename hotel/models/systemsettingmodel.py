from django.db import models
from hotel.models.visitormodel import Visitor
from hotel.models.roommodel import Room
from hotel.models.bookingmodel import Booking


class SystemSetting(models.Model):
    managed = True
    meta_key = models.CharField(max_length=50, unique=True, null=False, blank=False)
    meta_value = models.BooleanField()
    class Meta:
        db_table = "charta_system_setting"