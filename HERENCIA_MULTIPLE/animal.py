
class Animal:
    
   # Método constructor
    def __init__(self, peso, altura, alimentos):
      self._peso = peso
      self._altura = altura
      self._alimentos = alimentos

   # se definen los Setter y Getter
    def set_peso(self, peso):
      self._peso = peso

    def get_peso(self):
      return self._peso

    def set_altura(self, altura):
      self._altura = altura

    def get_altura(self):
      return self._altura

    def set_alimentos(self, alimentos):
      self._alimentos = alimentos

    def get_alimentos(self):
      return self._alimentos
   # Fin de los Setter y Getter

   # Calculo del Indice de Masa Muscular
    def get_imc(self):
      return self._peso / (self._altura * self._altura)
