from django.db import models
from django.contrib import admin

from stats.models.climb.climb_route_try import ClimbRouteTryRepository
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
        self.time_spent_climbing = QuerysetService.sum_field_of_queryset(sessions, 'duration')
        self.save()

    def count_success_climb_route(self, climb_route):
        climb_route_tries = ClimbRouteTryRepository.get_all()
        tries_correct_route = ClimbRouteTryRepository.filter_queryset_by_climb_route(
            queryset=climb_route_tries,
            climb_route=climb_route,
        )
        tries_correct_route_and_user = ClimbRouteTryRepository.filter_queryset_by_user(
            queryset=tries_correct_route,
            climb_user=self,
        )
        succeeded_route = ClimbRouteTryRepository.filter_queryset_by_success(
            queryset=tries_correct_route_and_user,
            is_success=True
        )
        return succeeded_route.count()

    def has_done_climb_route(self, climb_route):
        return self.count_success_climb_route(climb_route) > 0

    def is_first_time_climb_route(self, climb_route):
        return self.count_success_climb_route(climb_route) == 1


class ClimbUserInline(admin.StackedInline):
    model = ClimbUser

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


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


class ClimbUserRepository:
    @staticmethod
    def get_all():
        return ClimbUser.objects.all()
