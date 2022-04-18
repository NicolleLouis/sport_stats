from __future__ import annotations
from typing import TYPE_CHECKING

from stats.models.climb.climb_session_stat_color import ClimbSessionStatColorInline

if TYPE_CHECKING:
    from stats.models import ClimbSessionStatColor

from django.db import models
from django.contrib import admin

from stats.constants.route_color import RouteColor
from stats.models.climb.location import Location
from stats.service.date import DateService


class ClimbSession(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    climber = models.ForeignKey(
        'ClimbUser',
        on_delete=models.SET_NULL,
        null=True,
        related_name="sessions",
    )
    duration = models.IntegerField(
        default=60,
        verbose_name='Durée (en min)'
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
    )

    def __str__(self):
        created_at = DateService.convert_to_format(
            self.created_at,
            DateService.date_format
        )
        return f'{self.climber}: {created_at} - {self.location}'

    def get_related_stat_by_color(self, color: str) -> ClimbSessionStatColor | None:
        from stats.models.climb.climb_session_stat_color import ClimbSessionStatColorRepository

        all_stats = ClimbSessionStatColorRepository.get_all()
        session_stats = ClimbSessionStatColorRepository.filter_by_session(
            all_stats, self
        )
        color_session_stat = ClimbSessionStatColorRepository.filter_by_color(
            session_stats, color
        )
        if color_session_stat.count() == 0:
            return None
        return color_session_stat[0]

    def update_data(self):
        from stats.service.climb_session import ClimbSessionService

        session_stat_color_instances = ClimbSessionService.generate_session_stat_color_instance(self)
        for session_stat_by_color in session_stat_color_instances:
            session_stat_by_color.update_data()


@admin.register(ClimbSession)
class ClimbSessionAdmin(admin.ModelAdmin):
    list_display = (
        'climber',
        'duration',
        'location',
        'get_ratio_blue_session',
        'get_ratio_blue_location',
    )

    list_filter = (
        'climber',
        'location',
    )

    inlines = (
        ClimbSessionStatColorInline,
    )

    def get_ratio_blue_session(self, instance):
        blue_stats = instance.get_related_stat_by_color(RouteColor.BLUE)
        if blue_stats is None:
            return 0
        return blue_stats.ratio_route_session

    get_ratio_blue_session.short_description = 'Ratio bleues validées dans la séance'

    def get_ratio_blue_location(self, instance):
        blue_stats = instance.get_related_stat_by_color(RouteColor.BLUE)
        if blue_stats is None:
            return 0
        return blue_stats.ratio_route_location
    get_ratio_blue_location.short_description = 'Ratio bleues validées dans la salle'


class ClimbSessionRepository:
    @staticmethod
    def get_all_session():
        return ClimbSession.objects.all()

    @staticmethod
    def get_all_session_by_user(user):
        return ClimbSession.objects.filter(climber=user)

    @staticmethod
    def get_by_id(climb_session_id: int) -> ClimbSession:
        return ClimbSession.objects.get(id=climb_session_id)
