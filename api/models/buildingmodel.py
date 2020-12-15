from django.db import models

class Building(models.Model):
    managed = True
    name = models.CharField(max_length=255, unique=True, null=False, blank=False)
    code = models.CharField(max_length=10, default='', unique=True, null=True, blank=True)
    class Meta:
        db_table = "charta_building"