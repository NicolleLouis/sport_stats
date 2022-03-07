from django.core.management.base import BaseCommand, CommandError

from stats.models import ClimbUser


class Command(BaseCommand):
    def handle(self, *args, **options):
        users = ClimbUser.objects.all()
        for user in users:
            user.update_stats()
