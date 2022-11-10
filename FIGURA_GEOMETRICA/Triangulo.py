
from FiguraGeometrica import FiguraGeometrica

class Triangulo(FiguraGeometrica):

    def __init__(self, ancho, alto, color):
        FiguraGeometrica.__init__(self, ancho, alto)
        color.__init__(self, color)

    def calcular_area(self):
        return (self._alto * self._ancho) / 2

    def __str__(self) -> str:
        return f'{FiguraGeometrica.__str__(self)}'

