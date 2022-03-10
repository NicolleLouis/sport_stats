from django.db import models
from django.contrib import admin
from django.utils.safestring import mark_safe


class Location(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        null=True,
        max_length=24
    )
    blueprint = models.ImageField(
        upload_to='location/',
        null=True,
        blank=True,
    )
    number_of_sector = models.IntegerField(
        default=0
    )

    def __str__(self):
        return self.name


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'blueprint_image',
    )

    readonly_fields = (
        'blueprint_image',
    )

    def blueprint_image(self, instance):
        if instance.blueprint is not None:
            return mark_safe(
                '<img src="{url}" width="{width}" height={height} />'.format(
                    url=instance.blueprint.url,
                    width=instance.blueprint.width,
                    height=instance.blueprint.height,
                )
            )
        return None
