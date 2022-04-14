from django import forms

from stats.models.climb.climb_user import ClimbUserRepository


class ClimberForm(forms.Form):
    climber = forms.ModelChoiceField(
        queryset=ClimbUserRepository.get_all(),
        empty_label="(No user)",
        label='Grimpeur',
    )
