""" 

    2. Crea una clase llamada Linea con cuatro propiedades/atributos denominados x1, x2, y1 e y2, con constructor y con un método que obtenga el punto medio del segmento usando dichas propiedades/atributos. Crea 3 instancias/objetos de la clase Linea y ejecuta en ellos el método creado.


    @author Victor Fernandez España

"""

class Linea:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def puntoMedio(self):
        return ((self.x1 + self.x2) / 2, (self.y1 + self.y2) / 2)




punto1 = Linea(10, 20, 30, 40)
print(punto1.puntoMedio())

punto2 = Linea(50, 60, 70, 80)
print(punto2.puntoMedio())

punto3 = Linea(90, 100, 110, 120)
print(punto3.puntoMedio())