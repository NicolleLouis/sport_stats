from stats.models.climb.climb_session import ClimbSessionRepository


class ClimbUserStatColorService:
    @staticmethod
    def update_raw_values(climb_user_stat_color):
        sessions = ClimbSessionRepository.get_all_session_by_user(climb_user_stat_color.climb_user)
        sessions_stats = list(
            map(
                lambda session: session.get_related_stat_by_color(climb_user_stat_color.color),
                sessions
            )
        )
        not_empty_sessions_stats = list(
            filter(
                None,
                sessions_stats
            )
        )
        climb_user_stat_color.number_of_routes_succeeded = sum(
            map(
                lambda session_stat: session_stat.all_routes_succeeded,
                not_empty_sessions_stats
            )
        )
        climb_user_stat_color.number_of_routes_tried = sum(
            map(
                lambda session_stat: session_stat.routes_tried,
                not_empty_sessions_stats
            )
        )
        climb_user_stat_color.number_of_routes_flashed = sum(
            map(
                lambda session_stat: session_stat.routes_flashed,
                not_empty_sessions_stats
            )
        )
        climb_user_stat_color.save()
