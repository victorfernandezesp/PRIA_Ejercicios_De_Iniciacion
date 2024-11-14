"""
    21. Imprime los enteros recibidos reorganizados de tal manera que después de un 3 haya un 4. 
        Los treses no pueden cambiar de posición.

    @author Victor Fernandez España
"""

z = 1000
contador = 0
for x in range(1, z):
    for y in range(x + 1, z + 1):
        if (x + y) > 0 and (x * y) % (x + y) == 0:
            contador += 1
print(contador)
