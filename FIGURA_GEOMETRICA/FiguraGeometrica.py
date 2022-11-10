
from abc import ABC, abstractmethod

class FiguraGeometrica:
    def __init__(self, ancho, alto):
        if self._validar_valor(ancho):
          self._ancho = ancho
        else
          self._ancho = 0
          print('Error, el ancho de la figura no puede ser negativo')

        if self._validar_valor(alto):
          self._alto = alto
        else
          self._alto = alto
          print('Error, el alto de la figura no puede ser negativo')

    def set_ancho(self, ancho):
        self._ancho = ancho

    def get_ancho(self):
        returm self._ancho

    def set_alto(self, alto):
        self._alto = alto

    def get_alto(self):
        returm self._alto

    def _validar_valor(self, valor):
        return True if valor >= 0 else False

    @abstractmethod
    def calcular_area(self):
        pass

    def __str__(self) -> str:
       return f'Figura geométrica [Ancho: {self._ancho}, Alto: {self._alto}]'