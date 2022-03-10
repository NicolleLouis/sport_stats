from django.db import models
from django.contrib import admin

from stats.models import User
from stats.service.date import DateService


class Weight(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    weight = models.FloatField(
        null=True,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
    )

    def __str__(self):
        created_at = DateService.convert_to_format(
            self.created_at,
            DateService.date_format
        )
        return f'{self.user}: {self.weight} - {created_at}'


@admin.register(Weight)
class WeightAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'weight',
        'created_at',
    )

    list_filter = (
        'user',
    )
