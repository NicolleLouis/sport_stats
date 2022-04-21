class NotEnoughColorException(Exception):
    """
    Raised when a graph tries to use more color than we currently have
    """

    def __init__(self, index, *args):
        super().__init__(args)
        self.index = index

    def __str__(self):
        return f"You are asking for too many colors, please add more in chart.constants.color"
