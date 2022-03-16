from django import forms


class ClimbSessionClimbRouteForm(forms.Form):
    climb_route_id = forms.IntegerField(
        label='Route id',
        disabled=True,
        widget=forms.HiddenInput()
    )
    climb_route_picture_url = forms.CharField(
        label='Picture url',
        disabled=True,
        widget=forms.HiddenInput(),
    )
    sector = forms.IntegerField(
        label='Secteur',
        disabled=True,
    )
    is_tried = forms.BooleanField(
        initial=False,
        label='Essayée',
        required=False,
    )
    is_success = forms.BooleanField(
        initial=False,
        label='Réussie',
        required=False,
    )
    is_flashed = forms.BooleanField(
        initial=False,
        label='Flashée',
        required=False,
    )
