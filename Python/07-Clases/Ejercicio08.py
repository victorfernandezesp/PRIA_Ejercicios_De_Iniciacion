""" 

    8. Crea una clase llamada Forma con una propiedad/atributo denominada centro de tipo clase Punto y un método que se llame area y que devuelva un número, por ejemplo 0. A continuación, crea dos clases llamadas Rectangulo y Circulo (realizados en ejercicios 03 y 04) que hereden de la clase Forma ya creada. Crea 3 instancias/objetos de las clases Rectangulo, Circulo, de la clase que hereda Forma y ejecuta sus métodos.


    @author Victor Fernandez España

"""
from Ejercicio01 import Punto
from math import pi


class Forma:
    def __init__(self, centro):
        self.centro = centro
    
    def area(self: Punto):
        return 0
    

class Rectangulo(Forma):
    def __init__(self, centro, longitud, ancho):
        super().__init__(centro)
        self.longitud = longitud
        self.ancho = ancho
    
    def area(self):
        return self.longitud * self.ancho
    

class Circulo(Forma):
    def __init__(self, centro, radio):
        super().__init__(centro)
        self.radio = radio
    
    def area(self):
        return pi * self.radio ** 2


punto1 = Punto(10, 20)
rectangulo1 = Rectangulo(punto1, 30, 40)
print(rectangulo1.area())

punto2 = Punto(50, 60)
circulo1 = Circulo(punto2, 10)
print(circulo1.area())

punto3 = Punto(70, 80)
forma1 = Forma(punto3)
print(forma1.area())
