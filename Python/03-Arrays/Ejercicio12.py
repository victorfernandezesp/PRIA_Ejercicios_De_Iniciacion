""" 
    12. En una array 3x3 de enteros, muestra la suma más alta de los números de una fila.

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

suma_fila1 = array[0][0] + array[0][1] + array[0][2]
suma_fila2 = array[1][0] + array[1][1] + array[1][2]
suma_fila3 = array[2][0] + array[2][1] + array[2][2]
suma_maxima = max(suma_fila1, suma_fila2, suma_fila3)
print(suma_maxima)