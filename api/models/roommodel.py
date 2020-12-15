from django.db import models
from api.models.buildingmodel import Building


class Room(models.Model):
    managed = True
    name = models.CharField(max_length=255, unique=True, null=False, blank=False)
    code = models.CharField(max_length=10, default='', unique=True, null=True, blank=True)
    building = models.ForeignKey(Building, on_delete=models.SET_NULL, default=None, null=True, blank=True)
    class Meta:
        db_table = "charta_room"