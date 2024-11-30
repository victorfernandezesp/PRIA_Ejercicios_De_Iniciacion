""" 

    5. Crea una clase llamada Estudiante con dos propiedades/atributos denominados nombre y notas (array/lista), con constructor y con métodos que obtenga el nombre, modifique el nombre, obtenga las notas, modifique las notas y, por último, que obtenga la media de esas notas y las muestre. Crea 3 instancias/objetos de la clase Estudiante y ejecuta en ellos el método creado.


    @author Victor Fernandez España

"""

class Estudiante:
    def __init__(self, nombre, notas: list):
        self.nombre = nombre
        self.notas = notas

    def getNombre(self):
        return self.nombre
    
    def setNombre(self, nombre):
        self.nombre = nombre

    def getNotas(self):
        return self.notas

    def setNotas(self, notas):
        self.notas = notas

    def mediaNotas(self):
        return sum(self.notas) / len(self.notas)
    

estudiante1 = Estudiante("Victor", [10, 20, 30, 40, 50])
print(estudiante1.getNombre())
print(estudiante1.getNotas())
print(estudiante1.mediaNotas())

estudiante2 = Estudiante("Pepe", [60, 70, 80, 90, 100])
print(estudiante2.getNombre())
print(estudiante2.getNotas())
print(estudiante2.mediaNotas())

estudiante3 = Estudiante("Juan", [110, 120, 130, 140, 150])
print(estudiante3.getNombre())
print(estudiante3.getNotas())
print(estudiante3.mediaNotas())

