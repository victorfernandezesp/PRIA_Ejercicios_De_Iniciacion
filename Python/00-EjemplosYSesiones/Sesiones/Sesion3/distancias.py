""" 
    Resuelve en C# y Python los dos ejercicios de este vídeo sobre el teorema de Pitágoras (fórmula).



    @author Victor Fernandez España

"""

import math

punto1_2D, punto2_2D = (1, 2), (3, 4)

distancia_2D = math.sqrt(
    (punto2_2D[0] - punto1_2D[0]) ** 2 + (punto2_2D[1] - punto1_2D[1]) ** 2
)

punto1_3D, punto2_3D = (1, 2, 3), (4, 6, 8)

distancia_3D = math.sqrt(
    (punto2_3D[0] - punto1_3D[0]) ** 2
    + (punto2_3D[1] - punto1_3D[1]) ** 2
    + (punto2_3D[2] - punto1_3D[2]) ** 2
)

print("La distancia entre los puntos en 2D es:", distancia_2D)
print("La distancia entre los puntos en 3D es:", distancia_3D)
