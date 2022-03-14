from django.urls import path

from stats.views.climb_session.initial_climb_session import get_initial_data_climb_session

urlpatterns = [
    path('initial-climb-session/', get_initial_data_climb_session),
]
