""" 

    7. Crea una clase llamada Linea2D con dos propiedades/atributos denominados p1 y p2 de tipo clase Punto (realizado en ejercicio 01) y con dos métodos, uno que obtenga el punto medio del segmento y otro que obtenga la distancia euclídea, ambos usando dichas propiedades/atributos. Crea 3 instancias/objetos de la clase Linea2D y ejecuta en ellos los dos métodos creado.


    @author Victor Fernandez España

"""
from Ejercicio01 import Punto

class Linea2D:
    def __init__(self, p1: Punto, p2: Punto):
        self.p1 = p1
        self.p2 = p2

    def puntoMedio(self):
        return ((self.p1.getX() + self.p2.getX()) / 2, (self.p1.getY() + self.p2.getY()) / 2)
    
    def distanciaEuclidea(self):
        return ((self.p1.getX() - self.p2.getX()) ** 2 + (self.p1.getY() - self.p2.getY()) ** 2) ** 0.5
    
punto1 = Punto(10, 20)
punto2 = Punto(30, 40)
linea1 = Linea2D(punto1, punto2)
print(linea1.puntoMedio())
print(linea1.distanciaEuclidea())

punto3 = Punto(50, 60)
punto4 = Punto(70, 80)
linea2 = Linea2D(punto3, punto4)
print(linea2.puntoMedio())
print(linea2.distanciaEuclidea())

punto5 = Punto(90, 100)
punto6 = Punto(110, 120)
linea3 = Linea2D(punto5, punto6)
print(linea3.puntoMedio())
print(linea3.distanciaEuclidea())
   