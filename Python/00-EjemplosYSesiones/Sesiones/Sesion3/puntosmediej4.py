""" 
    Calcula en C# y Python la distancia y el punto medio entre los puntos (-1, -3) y (5, 7) en el espacio 2D.



    @author Victor Fernandez España

"""

import math

punto1, punto2 = (-1, -3), (5, 7)

distancia = math.sqrt((punto2[0] - punto1[0])**2 + (punto2[1] - punto1[1])**2)
punto_medio = ((punto1[0] + punto2[0]) / 2, (punto1[1] + punto2[1]) / 2)

print("La distancia entre los puntos es:", distancia)
print("El punto medio entre los puntos es:", punto_medio)
