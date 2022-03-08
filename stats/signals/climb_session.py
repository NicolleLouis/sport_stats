from django.db.models.signals import post_save
from django.dispatch import receiver

from stats.models import ClimbSession
from stats.service.climb_session import ClimbSessionService


@receiver(post_save, sender=ClimbSession)
def create_generic_sport_session(sender, instance, created, **kwargs):
    if not created:
        return
    ClimbSessionService.convert_into_sport_session(instance)
