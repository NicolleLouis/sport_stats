from django.db import models
from django.contrib import admin

from stats.service.date import DateService


class ClimbRoute(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(
        'Location',
        on_delete=models.SET_NULL,
        null=True,
    )
    sector = models.IntegerField(
        default=0,
    )
    is_active = models.BooleanField(
        default=True,
    )
    tags = models.ManyToManyField(
        'RouteTag',
        related_name='routes',
        blank=True,
    )

    def __str__(self):
        created_at = DateService.convert_to_format(
            self.created_at,
            DateService.date_format
        )
        return f'{self.location} sector: {self.sector} - {created_at}'


class RouteTagInline(admin.StackedInline):
    model = ClimbRoute.tags.through


@admin.register(ClimbRoute)
class ClimbRouteAdmin(admin.ModelAdmin):
    list_display = (
        'location',
        'sector',
        'is_active',
    )

    inlines = (
        RouteTagInline,
    )

    actions = (
        'remove',
    )

    @admin.action(description="Remove")
    def remove(self, request, queryset):
        queryset.update(is_active=False)
