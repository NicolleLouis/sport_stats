from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from stats.models import ClimbSession


class ClimbSessionService:
    climb_name = 'Escalade'

    @classmethod
    def convert_into_sport_session(cls, climb_session: ClimbSession) -> None:
        from stats.models import SportSession
        from stats.models.sport import SportRepository

        climb_sport = SportRepository.get_by_name(cls.climb_name)
        sport_session = SportSession(
            user=climb_session.climber.user,
            sport=climb_sport,
            duration=climb_session.duration,
        )
        sport_session.save()

    @staticmethod
    def compute_data_by_color(climb_session: ClimbSession, color) -> (int, int):
        from stats.models.climb.climb_route_try import ClimbRouteTryRepository

        climb_user = climb_session.climber
        routes = climb_session.routes_tried.all()
        blues = ClimbRouteTryRepository.filter_queryset_by_color(routes, color)
        routes_succeeded = ClimbRouteTryRepository.filter_queryset_by_success(blues, True)
        all_route = routes_succeeded.count()
        new_route = sum(
            list(
                map(
                    lambda blue_succeeded: climb_user.is_first_time_climb_route(
                        blue_succeeded.climb_route
                    ),
                    routes_succeeded
                )
            )
        )
        return all_route, new_route
