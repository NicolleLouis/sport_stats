from django import forms

from stats.models.climb.climb_user import ClimbUserRepository
from stats.models.climb.location import LocationRepository


class ClimbSessionBasicFieldForm(forms.Form):
    climber = forms.ModelChoiceField(
        queryset=ClimbUserRepository.get_all(),
        empty_label="(No user)",
        label='Grimpeur',
    )
    location = forms.ModelChoiceField(
        queryset=LocationRepository.get_all(),
        empty_label="(No location)",
        label='Salle',
    )
    duration = forms.IntegerField(
        label='Durée',
        initial=60,
    )
