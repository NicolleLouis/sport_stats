from django.db import models
from django.contrib import admin

from stats.models import User


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
        return f'{self.user}: {self.weight} - {self.created_at}'


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
