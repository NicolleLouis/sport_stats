from django.shortcuts import render

from chart.pie.chart import PieChart
from stats.models.user import UserRepository
from stats.service.stats.tag_radar import TagRadarService


class TagTriesRepartitionStatsView:
    @classmethod
    def get(cls, request, climber_id):
        climber = UserRepository.get_by_id(climber_id).climb_profile
        data = TagRadarService.aggregate_tag_data(climber).export_tries_data()
        chart = PieChart(
            raw_data=data
        )
        return render(request, 'single-chart.html', {
            'title': f'Répartition essais par tag pour: {climber.user.name}',
            'climber_id': climber_id,
            'chart': chart.export_chart(),
        })
