from django.urls import path

from stats.views.climb_session.create_climb_session import get_create_data_climb_session
from stats.views.climb_session.update_climb_session import UpdateClimbSessionView
from stats.views.home import home
from stats.views.stats.choose_climber import get_choose_climber

urlpatterns = [
    path('create-climb-session/', get_create_data_climb_session),
    path('update-climb-session/<int:climb_session_id>', UpdateClimbSessionView.get_update_climb_session),
    path('choose-climber/', get_choose_climber),
    path('', home),
]
