""" 

    10. Crea una clase C que herede de una clase B y que la clase B herede de A. La clase C heredará todos los métodos y atributos de B y B de A. Como mínimo, una función de A, de B y de C tienen que tener el mismo nombre pero que hagan cosas distintas. Crea 3 instancias/objetos de las clases A, B y C y ejecuta todos los métodos que hayas creado.




    @author Victor Fernandez España

"""

class A:
    def __init__(self):
        pass

    def metodo(self):
        print("Metodo de la clase A")

class B(A):
    def __init__(self):
        super().__init__()

    def metodo(self):
        print("Metodo de la clase B")

class C(B):
    def __init__(self):
        super().__init__()

    def metodo(self):
        print("Metodo de la clase C")

a = A()
a.metodo()

b = B()
b.metodo()

c = C()
c.metodo()
