"""
    Suponga que es el administrador de un zoológico, el cual debe matener diferentes tipos de animales 
    (Gorilas y Conejos), tenga en cuenta que un animal consta de peso y altura y que a cada animal se le 
    debe proporcionar uno o varios alimentos a consumir; también para cada animal se debe calcular su IMC; 
    Por último, a un conejo se le debe proporcionar un 
    diente principal y al gorila se le debe calcular el peso total de los alimento ya que puede consumir 
    varios de ellos.
"""

from animal import Animal
from animales.conejo import Conejo
from animales.gorila import Gorila

class Alimento:
   # Método constructor
    def __init__(self, gramos):
      self.__gramos = gramos

   # se definen los Setter y Getter
    def set_gramos(self, gramos):
      self.__gramos = gramos

    def get_peso(self):
      return self.__gramos
   # Fin de los Setter y Getter


conejo = Conejo(3, 0.2, ['Hierba',"Agua","Zanahoria","Cilantrillo fundillo"], "Colmillo")
print('Conejo')
print('------------')
print(conejo.get_peso())
print(conejo.get_altura())
print(conejo.get_imc())
print(conejo.get_alimentos())
print(conejo.get_diente())

print('\nGorila')
print('------------')
gorila = Gorila(80, 1.2, ['Banana',"Pera","Hierba"])
print(gorila.get_peso())
print(gorila.get_altura())
print(gorila.get_imc())
print(gorila.get_alimentos())

