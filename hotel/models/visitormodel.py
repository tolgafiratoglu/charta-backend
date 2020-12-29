from django.db import models
from hotel.models.roommodel import Room


class Visitor(models.Model):
    managed = True
    name = models.CharField(max_length=255, unique=False, null=False, blank=False)
    lastname = models.CharField(max_length=255, unique=False, null=False, blank=False)
    email = models.CharField(max_length=255, unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = "charta_visitor"