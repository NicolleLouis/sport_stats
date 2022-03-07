class QuerysetService:
    @staticmethod
    def sum_field_of_queryset(queryset, field_name):
        return sum(
            list(
                map(
                    lambda instance: getattr(instance, field_name),
                    queryset
                )
            )
        )
