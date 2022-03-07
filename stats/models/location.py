from django.db import models
from django.contrib import admin


class Location(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        null=True,
        max_length=24
    )

    def __str__(self):
        return self.name


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
