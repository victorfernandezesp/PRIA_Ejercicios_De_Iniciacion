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

mayorsuma = max(array, key=sum)

print(f"{mayorsuma}")

