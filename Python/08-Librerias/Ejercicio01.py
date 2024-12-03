""" 

    1. Calcula el ángulo que forman dos vectores 2D. Comprueba cómo se resuelve el problema aquí. Por ejemplo, el ángulo que forman un vector con coordenadas x1 = 5.45 e y1 = 1.12 y otro con coordenadas x2 = -3.86 e y2 = 4.32 es de 2.097 radianes o 120.168 grados. Pista: usa la siguiente implementación propuesta en la página: var angle = Math.atan2(vector2.y, vector2.x) - Math.atan2(vector1.y, vector1.x). Opcional: puedes usar como parámetros de entrada variables de tipo numérico o instancias de la clase Punto (realizada en el ejercicio 01 del boletín de ejercicios de Clases).

    @author Victor Fernandez España

"""

from math import atan2, degrees


class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def angulo(vector1, vector2):
        return degrees(atan2(vector2.y, vector2.x) - atan2(vector1.y, vector1.x))


vector1 = Punto(5.45, 1.12)
vector2 = Punto(-3.86, 4.32)
print(Punto.angulo(vector1, vector2))
