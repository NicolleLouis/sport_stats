from stats.models import SportSession, ClimbSession
from stats.models.sport import SportRepository


class ClimbSessionService:
    climb_name = 'Escalade'

    @classmethod
    def convert_into_sport_session(cls, climb_session: ClimbSession):
        climb_sport = SportRepository.get_by_name(cls.climb_name)
        sport_session = SportSession(
            user=climb_session.climber,
            sport=climb_sport,
            duration=climb_session.duration,
        )
        sport_session.save()
