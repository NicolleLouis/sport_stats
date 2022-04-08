from django.db import models
from django.contrib import admin
from django.utils.safestring import mark_safe

from stats.constants.route_color import RouteColor
from stats.service.date import DateService


class ClimbRoute(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(
        'Location',
        on_delete=models.SET_NULL,
        null=True,
    )
    sector = models.IntegerField(
        default=0,
    )
    color = models.CharField(
        max_length=4,
        choices=RouteColor.choices,
        default=RouteColor.BLUE,
    )
    is_active = models.BooleanField(
        default=True,
    )
    picture = models.ImageField(
        upload_to='route/',
        null=True,
        blank=True,
    )
    tags = models.ManyToManyField(
        'RouteTag',
        related_name='routes',
        blank=True,
    )

    def __str__(self):
        created_at = DateService.convert_to_format(
            self.created_at,
            DateService.date_format
        )
        return f'{self.location}: {self.color}, sector {self.sector} - {created_at}'

    def get_picture(self):
        if self.picture:
            return self.picture.url
        else:
            return 'No picture'


class RouteInline(admin.StackedInline):
    model = ClimbRoute


class RouteTagInline(admin.StackedInline):
    model = ClimbRoute.tags.through


@admin.register(ClimbRoute)
class ClimbRouteAdmin(admin.ModelAdmin):
    list_display = (
        'location',
        'sector',
        'color',
        'is_active',
        'picture_image',
    )

    inlines = (
        RouteTagInline,
    )

    actions = (
        'remove',
    )

    list_filter = (
        'is_active',
        'location',
        'color',
        'sector',
    )

    readonly_fields = (
        'picture_image',
    )

    def picture_image(self, instance):
        if instance.picture is not None:
            return mark_safe(
                '<img src="{url}" width="{width}" height={height} />'.format(
                    url=instance.picture.url,
                    width=instance.picture.width,
                    height=instance.picture.height,
                )
            )
        return None

    @admin.action(description="Remove")
    def remove(self, request, queryset):
        queryset.update(is_active=False)


class ClimbRouteRepository:
    @staticmethod
    def get_all():
        return ClimbRoute.objects.all()

    @staticmethod
    def filter_queryset_by_location(queryset, location):
        return queryset.filter(location=location)

    @staticmethod
    def filter_queryset_by_is_active(queryset, is_active):
        return queryset.filter(is_active=is_active)

    @staticmethod
    def filter_queryset_by_color(queryset, color):
        return queryset.filter(color=color)

    @staticmethod
    def get_by_id(climb_route_id):
        return ClimbRoute.objects.get(
            id=climb_route_id,
        )

    @staticmethod
    def sort_queryset_by_sector(queryset):
        return queryset.order_by('sector')
