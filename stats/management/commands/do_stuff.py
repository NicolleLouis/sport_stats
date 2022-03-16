from django.core.management.base import BaseCommand

from stats.models import ClimbSession, ClimbUser, ClimbRoute


class Command(BaseCommand):
    def handle(self, *args, **options):
        climb_session = ClimbSession.objects.all()[5]
        cecile = ClimbUser.objects.all()[1]
        print(climb_session)
        routes = ClimbRoute.objects.all()
        for route in routes:
            print(route)
            print(cecile.has_done_climb_route(route))
