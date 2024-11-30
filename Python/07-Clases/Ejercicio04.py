""" 

    4. Crea una clase llamada Circulo con una propiedad/atributo denominado radio, con constructor y con dos métodos que calculen el area del círculo y la circunferencia del círculo usando dichas propiedades/atributos. Crea 3 instancias/objetos de la clase Circulo y ejecuta en ellos los dos métodos creados.


    @author Victor Fernandez España

"""
from math import pi

class Circulo:
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        return  pi * self.radio ** 2
    
    def circunferencia(self):
        return 2 * pi * self.radio
    

circulo1 = Circulo(10)
print(circulo1.area())
print(circulo1.circunferencia())

circulo2 = Circulo(20)
print(circulo2.area())
print(circulo2.circunferencia())

circulo3 = Circulo(30)
print(circulo3.area())
print(circulo3.circunferencia())