from django.http import HttpResponseRedirect
from django.shortcuts import render

from stats.forms.climber import ClimberForm


def get_choose_climber(request):
    if request.method == 'POST':
        form = ClimberForm(request.POST)
        if form.is_valid():
            climber = form.cleaned_data['climber']
            return HttpResponseRedirect(f'/sport/home-climber-stats/{climber.user.id}')
    else:
        form = ClimberForm()

    return render(request, 'single_form.html', {
        'form': form,
        'url': '.',
        'title': 'Choose Climber'
    })
