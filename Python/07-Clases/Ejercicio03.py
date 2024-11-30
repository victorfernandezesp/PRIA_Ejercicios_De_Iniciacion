""" 

    3. Crea una clase llamada Rectangulo con dos propiedades/atributos denominados longitud y ancho, con constructor y con un método que calcule el area del rectángulo usando dichas propiedades/atributos. Crea 3 instancias/objetos de la clase Rectangulo y ejecuta en ellos el método creado.


    @author Victor Fernandez España

"""

class Rectangulo:
    def __init__(self, longitud, ancho):
        self.longitud = longitud
        self.ancho = ancho
    
    def area(self):
        return self.longitud * self.ancho
    

rectangulo1 = Rectangulo(10, 20)
print(rectangulo1.area())

rectangulo2 = Rectangulo(30, 40)
print(rectangulo2.area())

rectangulo3 = Rectangulo(50, 60)
print(rectangulo3.area())