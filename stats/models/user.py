from django.db import models
from django.contrib import admin

from stats.models.climb.climb_user import ClimbUserInline


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        null=True,
        blank=True,
        max_length=24
    )

    def __str__(self):
        return self.name


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

    inlines = (
        ClimbUserInline,
    )
