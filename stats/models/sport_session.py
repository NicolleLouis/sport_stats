from django.db import models
from django.contrib import admin


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
        return f'{self.user}: {self.created_at} - {self.sport}'


@admin.register(SportSession)
class SportSessionAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'sport',
        'duration',
    )
