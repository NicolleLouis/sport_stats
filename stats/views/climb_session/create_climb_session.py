from django.http import HttpResponseRedirect
from django.shortcuts import render

from stats.forms.climb_session.basic_field import ClimbSessionBasicFieldForm
from stats.models import ClimbSession


def get_create_data_climb_session(request):
    if request.method == 'POST':
        form = ClimbSessionBasicFieldForm(request.POST)
        if form.is_valid():
            climb_session = ClimbSession(
                climber=form.cleaned_data['climber'],
                location=form.cleaned_data['location'],
                duration=form.cleaned_data['duration'],
            )
            climb_session.save()
            return HttpResponseRedirect(f'/sport/update-climb-session/{climb_session.id}')
    else:
        form = ClimbSessionBasicFieldForm()

    return render(request, 'single_form.html', {
        'form': form,
        'url': '.',
        'title': 'Info générales de session'
    })
