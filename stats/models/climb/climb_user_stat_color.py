from django.db import models

from stats.constants.route_color import RouteColor
from django.contrib import admin

from stats.models.climb.climb_session import ClimbSessionRepository


class ClimbUserStatColor(models.Model):
    climb_user = models.ForeignKey(
        'ClimbUser',
        on_delete=models.CASCADE,
        related_name='color_stats',
    )
    color = models.CharField(
        max_length=4,
        choices=RouteColor.choices,
        default=RouteColor.BLUE,
    )
    number_of_routes_succeeded = models.IntegerField(
        default=0,
        verbose_name='Nombre total de pistes réussies',
    )
    number_of_routes_flashed = models.IntegerField(
        default=0,
        verbose_name='Nombre total de pistes flashées',
    )
    number_of_routes_tried = models.IntegerField(
        default=0,
        verbose_name='Nombre total de pistes ratées',
    )

    def __str__(self):
        return f'{self.climb_user.user.name} stats for {self.color}'

    def update_stats(self) -> None:
        sessions = ClimbSessionRepository.get_all_session_by_user(self.climb_user)
        sessions_stats = list(
            map(
                lambda session: session.get_related_stat_by_color(self.color),
                sessions
            )
        )
        not_empty_sessions_stats = list(
            filter(
                None,
                sessions_stats
            )
        )
        self.number_of_routes_succeeded = sum(
            map(
                lambda session_stat: session_stat.all_routes_succeeded,
                not_empty_sessions_stats
            )
        )
        self.save()


@admin.register(ClimbUserStatColor)
class ClimbUserStatColorAdmin(admin.ModelAdmin):
    list_display = (
        'climb_user',
        'color',
        'number_of_routes_succeeded',
        'number_of_routes_flashed',
        'number_of_routes_tried',
    )

    list_filter = (
        'climb_user',
        'color',
    )

    readonly_fields = (
        'number_of_routes_succeeded',
        'number_of_routes_flashed',
        'number_of_routes_tried',
    )


class ClimbUserStatColorInline(admin.StackedInline):
    model = ClimbUserStatColor
    extra = 0
    max_num = 2

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False
