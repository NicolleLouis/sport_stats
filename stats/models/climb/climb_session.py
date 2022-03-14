from django.db import models
from django.contrib import admin

from stats.models.climb.climb_route_try import RouteTryInline
from stats.models.climb.location import Location
from stats.service.date import DateService


class ClimbSession(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    climber = models.ForeignKey(
        'ClimbUser',
        on_delete=models.SET_NULL,
        null=True,
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
    new_blue = models.IntegerField(
        default=0,
        verbose_name='Nombre de nouvelles bleues'
    )
    all_blue = models.IntegerField(
        default=0,
        verbose_name='Toutes les bleues'
    )
    new_red = models.IntegerField(
        default=0,
        verbose_name='Nombre de nouvelles rouges'
    )
    all_red = models.IntegerField(
        default=0,
        verbose_name='Toutes les rouges'
    )

    def __str__(self):
        created_at = DateService.convert_to_format(
            self.created_at,
            DateService.date_format
        )
        return f'{self.climber}: {created_at} - {self.location}'


@admin.register(ClimbSession)
class ClimbSessionAdmin(admin.ModelAdmin):
    list_display = (
        'climber',
        'duration',
        'location',
        'new_blue',
        'all_blue',
    )

    inlines = (
        RouteTryInline,
    )


class ClimbSessionRepository:
    @staticmethod
    def get_all_session_by_user(user):
        return ClimbSession.objects.filter(climber=user)
