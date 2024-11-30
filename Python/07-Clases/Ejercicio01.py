""" 

    1. Crea una clase llamada Punto con dos propiedades/atributos denominados x e y, con constructor y con cuatro métodos (getter y setter), uno para obtener x, otro para obtener y, otro para modificar x y otro método para modificar y. Crea 3 instancias/objetos de la clase Punto y ejecuta en ellos los cuatro métodos creados.


    @author Victor Fernandez España

"""

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def setX(self, x):
        self.x = x
    
    def setY(self, y):
        self.y = y




punto1 = Punto(10, 20)
print(punto1.getX())
print(punto1.getY())
punto1.setX(30)
punto1.setY(40)
print(punto1.getX())
print(punto1.getY())

punto2 = Punto(50, 60)
print(punto2.getX())
print(punto2.getY())
punto2.setX(70)
punto2.setY(80)
print(punto2.getX())
print(punto2.getY())

punto3 = Punto(90, 100)
print(punto3.getX())
print(punto3.getY())
punto3.setX(110)
punto3.setY(120)
print(punto3.getX())
print(punto3.getY())
