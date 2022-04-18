from django.urls import path

from stats.views.climb_session.create_climb_session import get_create_data_climb_session
from stats.views.climb_session.update_climb_session import UpdateClimbSessionView
from stats.views.home import home
from stats.views.stats.choose_climber import get_choose_climber
from stats.views.stats.color_detail import ColorDetailClimberStatsView
from stats.views.stats.home_climber_stats import HomeClimberStatsView
from stats.views.stats.tag_radar import TagRadarStatsView

urlpatterns = [
    path('create-climb-session/', get_create_data_climb_session),
    path('update-climb-session/<int:climb_session_id>', UpdateClimbSessionView.get_update_climb_session),
    path('home-climber-stats/<int:climber_id>', HomeClimberStatsView.get_home_climber_stats),
    path('choose-climber/', get_choose_climber),
    path('color-detail/<int:climber_id>', ColorDetailClimberStatsView.get_color_details),
    path('radar-tag/<int:climber_id>', TagRadarStatsView.get_tag_radar),
    path('', home),
]
