
from Cuadrado import Cuadrado
from Triangulo import Triangulo

print('Creando objeto de tipo CUADRADO'.center(50,"-"))
cuadrado = Cuadrado(ancho = 5, alto = 8, color = "Rojo")
cuadrado.set_alto(9)
cuadrado.set_ancho(9)
print(f'Calculando el área del cuadrado {cuadrado.calcular_area()}')
print(cuadrado)

print('Creando objeto de tipo TRIANGULO'.center(50,"-"))
triangulo = Triangulo(ancho = 5, alto = 5, color = "Rojo")
triangulo.set_alto(7)
triangulo.set_ancho(9)
print(f'Calculando el área del triangulo {triangulo.calcular_area()}')
print(triangulo)