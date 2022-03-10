from django.db import models
from django.contrib import admin


class RouteTag(models.Model):
    id = models.AutoField(primary_key=True)
    tag = models.CharField(
        null=True,
        max_length=24
    )

    def __str__(self):
        return self.tag


@admin.register(RouteTag)
class RouteTagAdmin(admin.ModelAdmin):
    list_display = (
        'tag',
    )

