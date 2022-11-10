
class Color:

    def __init__(self, color):
        self._color = color

    def set_color(self, color):
        self._color = color

    def get_color(self):
        return self._color

    def __str__(self) -> str:
        f'Color: [{self._color}]'