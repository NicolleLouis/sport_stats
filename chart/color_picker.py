import random

from constants.colors import colors


class ColorPicker:
    colors = colors

    @classmethod
    def get_random_color(cls):
        return random.choice(cls.colors)

    @classmethod
    def get_color(cls, index):
        return cls.colors[index]
