from django.db import models
from django.contrib import admin

from stats.service.date import DateService


class SportSession(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        'User',
        on_delete=models.SET_NULL,
        null=True,
    )
    sport = models.ForeignKey(
        'Sport',
        on_delete=models.SET_NULL,
        null=True,
    )
    duration = models.IntegerField(
        default=60,
        verbose_name='Durée (en min)'
    )

    def __str__(self):
        created_at = DateService.convert_to_format(
            self.created_at,
            DateService.date_format
        )
        return f'{self.user}: {created_at} - {self.sport}'


@admin.register(SportSession)
class SportSessionAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'sport',
        'duration',
    )
