import json

from django.shortcuts import render

from stats.models.user import UserRepository


class TagRadarStatsView:
    @classmethod
    def get_tag_radar(cls, request, climber_id):
        climber = UserRepository.get_by_id(climber_id).climb_profile
        chart = json.dumps({
                "type": 'radar',
                "data": {
                    "labels": ["charles", "victoire", "louis"],
                    "datasets": [
                        {
                            "label": "oui",
                            'fill': True,
                            "data": [1, 2, 3]
                        }
                    ]
                }
        })
        return render(request, 'single-chart.html', {
            'title': f'Ratio réussi/essayé par tag pour: {climber.user.name}',
            'climber_id': climber_id,
            'chart': chart,
        })
