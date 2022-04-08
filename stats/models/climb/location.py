from django.db import models
from django.contrib import admin
from django.utils.safestring import mark_safe

from stats.models.climb.climb_route import ClimbRouteRepository


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

    def get_all_active_route_by_color(self, color):
        all_routes = ClimbRouteRepository.get_all()
        all_active_route = ClimbRouteRepository.filter_queryset_by_is_active(
            all_routes,
            True
        )
        all_routes_by_color = ClimbRouteRepository.filter_queryset_by_color(
            all_active_route,
            color
        )
        all_routes_at_location = ClimbRouteRepository.filter_queryset_by_location(
            all_routes_by_color,
            self
        )
        return all_routes_at_location

    def number_of_active_route_by_color(self, color):
        return self.get_all_active_route_by_color(color).count()


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


class LocationRepository:
    @staticmethod
    def get_all():
        return Location.objects.all()
