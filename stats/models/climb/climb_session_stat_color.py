from django.db import models
from django.contrib import admin

from stats.constants.route_color import RouteColor
from stats.service.climb_session_stat_color import ClimbSessionStatColorService


class ClimbSessionStatColor(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    climb_session = models.ForeignKey(
        'ClimbSession',
        on_delete=models.CASCADE,
        null=True,
    )
    color = models.CharField(
        max_length=4,
        choices=RouteColor.choices,
        default=RouteColor.BLUE,
    )
    routes_tried = models.IntegerField(
        default=0,
        verbose_name='Nombre de pistes essayées',
    )
    routes_flashed = models.IntegerField(
        default=0,
        verbose_name='Nombre de pistes flashées',
    )
    new_routes_succeeded = models.IntegerField(
        default=0,
        verbose_name='Nombre de nouvelles pistes réussies',
    )
    all_routes_succeeded = models.IntegerField(
        default=0,
        verbose_name='Toutes les pistes réussies',
    )
    ratio_route_session = models.IntegerField(
        default=0,
        verbose_name='Ratio de pistes grimpée dans la séance'
    )
    ratio_route_location = models.IntegerField(
        default=0,
        verbose_name='Ratio de pistes validées dans la salle'
    )

    def __str__(self):
        return f'{self.climb_session} stats for {self.color}'

    def update_data(self):
        ClimbSessionStatColorService.compute_data(
            climb_session_stat_color=self
        )


@admin.register(ClimbSessionStatColor)
class ClimbSessionStatColorAdmin(admin.ModelAdmin):
    list_display = (
        'climb_session',
        'color',
        'new_routes_succeeded',
        'all_routes_succeeded',
        'routes_flashed',
        'routes_tried',
        'ratio_route_session',
        'ratio_route_location',
    )

    list_filter = (
        'color',
    )

    readonly_fields = (
        'climb_session',
        'color',
        'new_routes_succeeded',
        'all_routes_succeeded',
        'routes_flashed',
        'routes_tried',
        'ratio_route_session',
        'ratio_route_location',
    )


class ClimbSessionStatColorInline(admin.StackedInline):
    model = ClimbSessionStatColor
    extra = 0
    max_num = 2

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


class ClimbSessionStatColorRepository:
    @staticmethod
    def get_all():
        return ClimbSessionStatColor.objects.all()

    @staticmethod
    def filter_by_session(queryset, climb_session):
        return queryset.filter(climb_session=climb_session)

    @staticmethod
    def filter_by_color(queryset, color):
        return queryset.filter(color=color)
