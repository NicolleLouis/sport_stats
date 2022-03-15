from django.forms import formset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render

from stats.forms.climb_session.climb_route import ClimbSessionClimbRouteForm
from stats.models.climb.climb_route import ClimbRouteRepository
from stats.models.climb.climb_route_try import ClimbRouteTryRepository
from stats.models.climb.climb_session import ClimbSessionRepository


class UpdateClimbSessionView:
    @classmethod
    def get_update_climb_session(cls, request, climb_session_id):
        ClimbRouteFormSet = formset_factory(ClimbSessionClimbRouteForm, extra=0)
        climb_session = ClimbSessionRepository.get_by_id(climb_session_id)

        initial_data = cls.generate_initial_data(climb_session)
        if request.method == 'POST':
            formset = ClimbRouteFormSet(request.POST, initial=initial_data)
            if formset.is_valid():
                for climb_route_form in formset:
                    cls.compute_form(climb_route_form, climb_session)

            return HttpResponseRedirect('/admin')
        else:
            formset = ClimbRouteFormSet(
                initial=initial_data
            )

            return render(request, 'update_session_route.html', {
                'title': 'Update Piste Session',
                'formset': formset,
                'url': f'./{climb_session_id}',
            })

    @staticmethod
    def generate_initial_data(climb_session):
        location = climb_session.location
        climb_routes = ClimbRouteRepository.get_all_active_by_location(location)
        return list(
            map(
                lambda climb_route: {
                    'climb_route_id': climb_route.id,
                    'sector': climb_route.sector,
                    'climb_route_picture_url': climb_route.picture.url,
                },
                climb_routes
            )
        )

    @staticmethod
    def compute_form(climb_route_form, climb_session):
        climb_route_id = climb_route_form.cleaned_data.get('climb_route_id')
        is_tried = climb_route_form.cleaned_data.get('is_tried')
        is_success = climb_route_form.cleaned_data.get('is_success')
        is_flashed = climb_route_form.cleaned_data.get('is_flashed')
        if is_tried:
            climb_route = ClimbRouteRepository.get_by_id(climb_route_id)
            climb_route_try = ClimbRouteTryRepository.get_or_create_by_session_and_route(
                climb_session=climb_session,
                climb_route=climb_route,
            )
            climb_route_try.is_flashed = is_flashed
            climb_route_try.is_success = is_success
            climb_route_try.save()
