from django.shortcuts import render

from stats.models.user import UserRepository
from stats.service.stats.raw_values import RawValueService


class HomeClimberStatsView:
    @classmethod
    def get_home_climber_stats(cls, request, climber_id):
        climber = UserRepository.get_by_id(climber_id).climb_profile
        aggregated_values = RawValueService.aggregate_raw_values_color(climber_id=climber_id)
        return render(request, 'home_climber_stats.html', {
            'title': f'Statistics: {climber.user.name}',
            'climber_id': climber_id,
            'aggregated_values': aggregated_values,
        })
