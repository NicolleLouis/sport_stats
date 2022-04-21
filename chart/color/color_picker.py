import random

from chart.color.not_enough_color_exception import NotEnoughColorException
from chart.constants.colors import colors


class ColorPicker:
    colors = colors

    @classmethod
    def get_random_color(cls):
        return random.choice(cls.colors)

    @classmethod
    def get_color(cls, index):
        if index >= len(cls.colors):
            raise NotEnoughColorException(index)

        return cls.colors[index]
