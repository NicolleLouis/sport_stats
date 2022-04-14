from django.shortcuts import render

from stats.models.user import UserRepository


class HomeClimberStatsView:
    @classmethod
    def get_home_climber_stats(cls, request, climber_id):
        climber = UserRepository.get_by_id(climber_id).climb_profile
        return render(request, 'home_climber_stats.html', {
            'title': f'Statistics: {climber.user.name}',
        })
