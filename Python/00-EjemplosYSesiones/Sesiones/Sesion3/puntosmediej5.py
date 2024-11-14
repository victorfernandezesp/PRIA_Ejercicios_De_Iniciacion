""" 
    Calcula en C# y Python la distancia y el punto medio entre A(-3, 4, -2) y B(2, 6, 3) en el espacio 3D.



    @author Victor Fernandez España

"""

import math

A, B = (-3, 4, -2), (2, 6, 3)

distancia = math.sqrt((B[0] - A[0])**2 + (B[1] - A[1])**2 + (B[2] - A[2])**2)
punto_medio = ((A[0] + B[0]) / 2, (A[1] + B[1]) / 2, (A[2] + B[2]) / 2)

print("La distancia entre A y B es:", distancia)
print("El punto medio entre A y B es:", punto_medio)
