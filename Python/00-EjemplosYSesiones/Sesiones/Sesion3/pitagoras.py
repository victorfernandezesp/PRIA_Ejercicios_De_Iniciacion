""" 
    Resuelve en C# y Python los dos ejercicios de este vídeo sobre el teorema de Pitágoras (fórmula).



    @author Victor Fernandez España

"""


import math

cateto1, cateto2 = 5, 6
cateto3, cateto4 = 20 * 10, 29 * 10

hipotenusa1 = math.sqrt(cateto1**2 + cateto2**2)
hipotenusa2 = math.sqrt(cateto3**2 + cateto4**2)

print("La hipotenusa en el ejercicio a:", hipotenusa1, "m")
print("La hipotenusa en el ejercicio b:", hipotenusa2, "m")
