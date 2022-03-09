from django.db import models
from django.contrib import admin

from stats.models.climb.climb_session import ClimbSessionRepository
from stats.service.queryset import QuerysetService


class ClimbUser(models.Model):
    user = models.OneToOneField(
        'User',
        on_delete=models.CASCADE,
        primary_key=True,
    )
    number_of_session = models.IntegerField(
        default=0,
        verbose_name='Nombre de séance',

    )
    number_of_blues = models.IntegerField(
        default=0,
        verbose_name='Nombre total de bleue',
    )
    number_of_red = models.IntegerField(
        default=0,
        verbose_name='Nombre total de rouge',
    )
    time_spent_climbing = models.IntegerField(
        default=0,
        verbose_name='Temps passé à grimper (en min)',
    )

    def __str__(self):
        return f'{self.user.name}'

    def update_stats(self) -> None:
        sessions = ClimbSessionRepository.get_all_session_by_user(self)
        self.number_of_session = sessions.count()
        self.number_of_blues = QuerysetService.sum_field_of_queryset(sessions, 'all_blue')
        self.number_of_red = QuerysetService.sum_field_of_queryset(sessions, 'all_red')
        self.time_spent_climbing = QuerysetService.sum_field_of_queryset(sessions, 'duration')
        self.save()


@admin.register(ClimbUser)
class ClimbUserAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'number_of_blues',
        'time_spent_climbing',
        'number_of_session',
    )

    readonly_fields = (
        'number_of_blues',
        'number_of_red',
        'time_spent_climbing',
        'number_of_session',
    )

    actions = (
        'update',
    )

    @admin.action(description="Update")
    def update(self, request, queryset):
        for climb_user in queryset:
            climb_user.update_stats()


class ClimbUserInline(admin.StackedInline):
    model = ClimbUser

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False
