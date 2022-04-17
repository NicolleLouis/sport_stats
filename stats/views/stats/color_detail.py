from django.shortcuts import render

from stats.models.user import UserRepository


class ColorDetailClimberStatsView:
    @classmethod
    def get_color_details(cls, request, climber_id):
        climber = UserRepository.get_by_id(climber_id).climb_profile
        color_stats = climber.color_stats.all()
        return render(request, 'color_details.html', {
            'title': f'Color Detail: {climber.user.name}',
            'climber_id': climber_id,
            'color_stats': color_stats,
        })
