
from animal import Animal

class Conejo(Animal):

   # Mëtodo Constructor
    def __init__(self, peso, altura, alimentos, diente):
      super().__init__(peso, altura, alimentos)
      self._diente = diente

   # se definen los Setter y Getter
    def set_diente(self, diente):
      self._diente = diente

    def get_diente(self):
      return self._diente
   # Fin de los Setter y Getter
