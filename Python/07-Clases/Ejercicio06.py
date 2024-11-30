""" 

    6. Crea una función que reciba dos parámetros de entrada de tipo clase Punto (realizado en ejercicio 01) y que devuelva la distancia euclídea entre esos dos puntos. Ejecuta 3 llamadas de ejemplo de la función creada.


    @author Victor Fernandez España

"""

from math import sqrt

from Ejercicio01 import Punto

def distanciaEuclidea(punto1, punto2):
    return sqrt((punto1.getX() - punto2.getX()) ** 2 + (punto1.getY() - punto2.getY()) ** 2)

punto1 = Punto(10, 20)
punto2 = Punto(30, 40)
print(distanciaEuclidea(punto1, punto2))

punto3 = Punto(50, 60)
punto4 = Punto(70, 80)
print(distanciaEuclidea(punto3, punto4))

punto5 = Punto(90, 100)
punto6 = Punto(110, 120)
print(distanciaEuclidea(punto5, punto6))