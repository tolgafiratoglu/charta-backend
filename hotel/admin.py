from django.contrib import admin

from hotel.models.buildingmodel import Building
from hotel.models.roomtypemodel import RoomType
from hotel.models.roommodel import Room

# Register your models here.
admin.site.register(Building)
admin.site.register(RoomType)
admin.site.register(Room)