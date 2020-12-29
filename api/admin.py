from django.contrib import admin

from api.models.buildingmodel import Building
from api.models.roomtypemodel import RoomType
from api.models.roommodel import Room

# Register your models here.
admin.site.register(Building)
admin.site.register(RoomType)
admin.site.register(Room)