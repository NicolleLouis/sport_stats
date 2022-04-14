from django.core.management.base import BaseCommand

from stats.models.climb.climb_session_stat_color import ClimbSessionStatColorRepository


class Command(BaseCommand):
    def handle(self, *args, **options):
        all_climb_session_stat = ClimbSessionStatColorRepository.get_all()
        for stat in all_climb_session_stat:
            print(stat)