from django.db import models
from django.contrib import admin


class ClimbRouteTry(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    climb_session = models.ForeignKey(
        'ClimbSession',
        on_delete=models.CASCADE,
        null=True,
        related_name='routes_tried',
    )
    climb_route = models.ForeignKey(
        'ClimbRoute',
        on_delete=models.CASCADE,
        null=True,
    )
    is_success = models.BooleanField(
        default=True,
        verbose_name='Réussie?'
    )
    is_flashed = models.BooleanField(
        default=False,
        verbose_name='Flashée?'
    )

    @property
    def climber(self):
        return self.climb_session.climber

    def __str__(self):
        success_message = 'Grimpée' if self.is_success else 'Essayée'
        return f'{self.climber}: {success_message} - {self.climb_route}'

    class Meta:
        unique_together = [['climb_session', 'climb_route']]


class RouteTryInline(admin.StackedInline):
    model = ClimbRouteTry


@admin.register(ClimbRouteTry)
class ClimbRouteTryAdmin(admin.ModelAdmin):
    list_display = (
        'climber',
        'climb_route',
        'is_success',
        'is_flashed',
    )

    list_filter = (
        'is_success',
        'is_flashed',
    )

    @admin.display(description='Grimpeur')
    def climber(self, instance: ClimbRouteTry):
        return instance.climber


class ClimbRouteTryRepository:
    @staticmethod
    def get_or_create_by_session_and_route(climb_session, climb_route):
        climb_route_try, _created = ClimbRouteTry.objects.get_or_create(
            climb_route=climb_route,
            climb_session=climb_session
        )
        return climb_route_try

    @staticmethod
    def get_all():
        return ClimbRouteTry.objects.all()

    @staticmethod
    def filter_queryset_by_color(queryset, color):
        return queryset.filter(climb_route__color=color)

    @staticmethod
    def filter_queryset_by_success(queryset, is_success):
        return queryset.filter(is_success=is_success)

    @staticmethod
    def filter_queryset_by_user(queryset, climb_user):
        return queryset.filter(climb_session__climber=climb_user)

    @staticmethod
    def filter_queryset_by_climb_route(queryset, climb_route):
        return queryset.filter(climb_route=climb_route)
