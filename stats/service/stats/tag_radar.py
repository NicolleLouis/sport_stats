class TagTryData:
    def __init__(self, tag):
        self.tag = tag
        self.tried = 0
        self.succeeded = 0
        self.flashed = 0
        self.ratio_succeeded = 0
        self.ratio_flashed = 0

    def add_route_try(self, route_try):
        self.tried += 1
        if route_try.is_success:
            self.succeeded += 1
        if route_try.is_flashed:
            self.flashed += 1

    def compute_ratio(self):
        if self.tried == 0:
            return
        self.ratio_succeeded = self.succeeded / self.tried
        self.ratio_flashed = self.flashed / self.tried


class TagTriesAggregation:
    def __init__(self):
        self.aggregated_data = {}

    def add_try_for_tag(self, tag, route_try):
        if tag not in self.aggregated_data:
            self.aggregated_data[tag] = TagTryData(tag=tag)
        self.aggregated_data[tag].add_route_try(route_try)

    def add_try(self, route_try):
        tags = route_try.climb_route.tags.all()
        for tag in tags:
            self.add_try_for_tag(tag, route_try)

    def export_data(self):
        ratio_succeeded = {}
        ratio_flashed = {}
        for tag in self.aggregated_data:
            tag_data = self.aggregated_data[tag]
            tag_data.compute_ratio()
            ratio_succeeded[tag.tag] = tag_data.ratio_succeeded
            ratio_flashed[tag.tag] = tag_data.ratio_flashed
        return {
            "Ratio Réussite": ratio_succeeded,
            "Ratio Flashé": ratio_flashed,
        }


class TagRadarService:
    @staticmethod
    def compute_tag_ratio(climber):
        aggregation = TagTriesAggregation()
        route_tries = []
        for session in climber.sessions.all():
            route_tries.extend(session.routes_tried.all())
        for route_try in route_tries:
            aggregation.add_try(route_try)
        return aggregation.export_data()

