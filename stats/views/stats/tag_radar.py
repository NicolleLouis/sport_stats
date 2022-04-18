from django.shortcuts import render

from chart.radio.chart import RadioChart
from stats.models.user import UserRepository
from stats.service.stats.tag_radar import TagRadarService


class TagRadarStatsView:
    @classmethod
    def get_tag_radar(cls, request, climber_id):
        climber = UserRepository.get_by_id(climber_id).climb_profile
        data = TagRadarService.compute_tag_ratio(climber)
        chart = RadioChart(
            raw_data=data
        )
        return render(request, 'single-chart.html', {
            'title': f'Ratio réussi/essayé par tag pour: {climber.user.name}',
            'climber_id': climber_id,
            'chart': chart.export_chart(),
        })
