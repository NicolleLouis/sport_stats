import json

from django.shortcuts import render

from chart.radio.chart import RadioChart
from stats.models.user import UserRepository


class TagRadarStatsView:
    @classmethod
    def get_tag_radar(cls, request, climber_id):
        climber = UserRepository.get_by_id(climber_id).climb_profile
        data = {
            "Ratio": {
                "Equilibre": 0.3,
                "Force": 0.8,
                "Module": 0.5,
            }
        }
        chart = RadioChart(
            raw_data=data
        )
        # [{"label": dataset_label, "data": dataset_data}, ...]
        # dataset follows this pattern: {"label": value, ...}
        return render(request, 'single-chart.html', {
            'title': f'Ratio réussi/essayé par tag pour: {climber.user.name}',
            'climber_id': climber_id,
            'chart': chart.export_chart(),
        })
