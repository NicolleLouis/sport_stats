from stats.models.user import UserRepository


class AggregatedValue:
    def __init__(
            self,
            number_of_routes_succeeded,
            number_of_routes_flashed,
            number_of_routes_tried,
    ):
        self.number_of_routes_succeeded = number_of_routes_succeeded
        self.number_of_routes_flashed = number_of_routes_flashed
        self.number_of_routes_tried = number_of_routes_tried


class RawValueService:
    @staticmethod
    def aggregate_raw_values_color(climber_id):
        climber = UserRepository.get_by_id(climber_id).climb_profile
        color_stats = climber.color_stats.all()
        number_of_routes_succeeded = 0
        number_of_routes_flashed = 0
        number_of_routes_tried = 0
        for color_stat in color_stats:
            number_of_routes_succeeded += color_stat.number_of_routes_succeeded
            number_of_routes_tried += color_stat.number_of_routes_tried
            number_of_routes_flashed += color_stat.number_of_routes_flashed
        aggregated_values = AggregatedValue(
            number_of_routes_succeeded=number_of_routes_succeeded,
            number_of_routes_flashed=number_of_routes_flashed,
            number_of_routes_tried=number_of_routes_tried,
        )
        return aggregated_values
