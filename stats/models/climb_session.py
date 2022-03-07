from django.db import models
from django.contrib import admin

from stats.models.user import User
from stats.models.location import Location


class ClimbSession(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    climber = models.ForeignKey(
        User,
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
        return f'{self.climber}: {self.created_at} - {self.location}'


@admin.register(ClimbSession)
class ClimbSessionAdmin(admin.ModelAdmin):
    list_display = (
        'climber',
        'duration',
        'location',
        'new_blue',
        'all_blue',
    )
