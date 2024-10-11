""" 
    12. En una matriz 3x3 de enteros, muestra la suma más alta de los números de una fila.

    @author Victor Fernandez España

"""
array = [[],[],[]]
numero = int(input("Introduce un número:    "))
array[0].append(numero)
numero = int(input("Introduce un número:    "))
array[0].append(numero)
numero = int(input("Introduce un número:    "))
array[0].append(numero)
numero = int(input("Introduce un número:    "))
array[1].append(numero)
numero = int(input("Introduce un número:    "))
array[1].append(numero)
numero = int(input("Introduce un número:    "))
array[1].append(numero)
numero = int(input("Introduce un número:    "))
array[2].append(numero)
numero = int(input("Introduce un número:    "))
array[2].append(numero)
numero = int(input("Introduce un número:    "))
array[2].append(numero)

print(f"Array sin modificar:    {array}")
array[0].sort
array[1].sort
array[2].sort
array[0].reverse()
array[1].reverse()
array[2].reverse()
array[0].pop()
array[1].pop()
array[2].pop()

print(f"Array sin modificar:    {array}")
print(f"Suma mas alta de la fila 1:       {array[0][0] + array[0][1]}")
print(f"Suma mas alta de la fila 2:       {array[1][0] + array[1][1]}")
print(f"Suma mas alta de la fila 3:       {array[2][0] + array[2][1]}")