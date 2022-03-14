class DateService:
    date_format = '%d %B %Y'

    @staticmethod
    def convert_to_format(datetime, date_format):
        return datetime.strftime(date_format)
