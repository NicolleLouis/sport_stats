from __future__ import annotations
from typing import TYPE_CHECKING

from stats.constants.route_color import RouteColor
from stats.models import ClimbSessionStatColor

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
    def generate_session_stat_color_instance(climb_session: ClimbSession):
        colors = [
            RouteColor.RED,
            RouteColor.BLUE,
        ]

        session_stat_color_instances = []

        for color in colors:
            climb_session_stat_color = ClimbSessionStatColor(
                color=color,
                climb_session=climb_session,
            )
            session_stat_color_instances.append(climb_session_stat_color)

        return session_stat_color_instances
