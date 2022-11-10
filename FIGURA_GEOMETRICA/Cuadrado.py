#from Color import Color
from FiguraGeometrica import FiguraGeometrica


class Cuadrado(FiguraGeometrica):

    def __init__(self, ancho, alto, color):
        FiguraGeometrica.__init__(self, ancho, alto)
       # color.__init__(self, color)

   # implementando el método abstracto de la clase FiguraGeometrica 
    def calcular_area(self):
        return self._alto * self._ancho

    def __str__(self) -> str:
        return f"{FiguraGeometrica.__str__(self)}"