from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from stats.models import ClimbSessionStatColor


class ClimbSessionStatColorService:
    @classmethod
    def compute_data(
            cls,
            climb_session_stat_color: ClimbSessionStatColor,
    ) -> None:
        cls.compute_raw_number(
            climb_session_stat_color=climb_session_stat_color,
        )
        cls.compute_ratio_session(
            climb_session_stat_color=climb_session_stat_color,
        )
        cls.compute_ratio_location(
            climb_session_stat_color=climb_session_stat_color,
        )
        return None

    @staticmethod
    def compute_raw_number(climb_session_stat_color: ClimbSessionStatColor) -> None:
        from stats.models.climb.climb_route_try import ClimbRouteTryRepository

        climb_session = climb_session_stat_color.climb_session
        color = climb_session_stat_color.color
        climb_user = climb_session.climber
        routes = climb_session.routes_tried.all()
        colored_routes = ClimbRouteTryRepository.filter_queryset_by_color(routes, color)
        climb_session_stat_color.routes_tried = colored_routes.count()
        routes_succeeded = ClimbRouteTryRepository.filter_queryset_by_success(colored_routes, True)
        climb_session_stat_color.all_routes_succeeded = routes_succeeded.count()
        climb_session_stat_color.new_routes_succeeded = sum(
            list(
                map(
                    lambda route_succeeded: climb_user.is_first_time_climb_route(
                        route_succeeded.climb_route
                    ),
                    routes_succeeded
                )
            )
        )
        routes_flashed = ClimbRouteTryRepository.filter_queryset_by_flashed(
            colored_routes,
            True
        )
        climb_session_stat_color.routes_flashed = routes_flashed.count()
        climb_session_stat_color.save()

    @staticmethod
    def compute_ratio_session(
            climb_session_stat_color: ClimbSessionStatColor,
    ) -> None:
        color = climb_session_stat_color.color
        climb_session = climb_session_stat_color.climb_session
        location = climb_session.location
        total_route_number = location.number_of_active_route_by_color(color)
        route_climbed = climb_session_stat_color.all_routes_succeeded
        if total_route_number == 0:
            ratio = 0
        else:
            ratio = round(100 * route_climbed / total_route_number)

        climb_session_stat_color.ratio_route_session = ratio
        climb_session_stat_color.save()

    @staticmethod
    def compute_ratio_location(
            climb_session_stat_color: ClimbSessionStatColor,
    ) -> None:
        color = climb_session_stat_color.color
        climb_session = climb_session_stat_color.climb_session
        climb_user = climb_session.climber
        location = climb_session.location
        total_route_number = location.number_of_active_route_by_color(color)
        all_location_route = location.get_all_active_route_by_color(color)
        route_climbed = sum(
            list(
                map(
                    lambda route_succeeded: climb_user.has_done_climb_route(
                        route_succeeded
                    ),
                    all_location_route
                )
            )
        )
        if total_route_number == 0:
            ratio = 0
        else:
            ratio = round(100 * route_climbed / total_route_number)

        climb_session_stat_color.ratio_route_location = ratio
        climb_session_stat_color.save()
