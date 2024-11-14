""" 
    1. Crea un programa que:

    Sume todos los elementos (de tipo numérico) de un array, o lista, mediante un bucle.
    Multiplique todos los elementos (de tipo numérico) de un array, o lista, mediante un bucle.


    @author Victor Fernandez España

"""

array = [1, 2, 3, 4, 5]

acumulador = 0
acumulador2 = 1

for i in array:
    acumulador += i

for i in array:
    acumulador2 *= i

print(f"Suma:   {acumulador}")
print(f"Multiplicacion:     {acumulador2}")