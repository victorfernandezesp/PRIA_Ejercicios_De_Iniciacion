""" 
    17. Dada una lista impar de enteros ordenados, muestra la mediana.


    @author Victor Fernandez España

"""
import statistics

array = []
numero = int(input("Escribe el númmero:     "))
array.append(numero)
numero = int(input("Escribe el númmero:     "))
array.append(numero)
numero = int(input("Escribe el númmero:     "))
array.append(numero)
numero = int(input("Escribe el númmero:     "))
array.append(numero)
numero = int(input("Escribe el númmero:     "))
array.append(numero)

array.sort()
medianaNum = statistics.median(array)
print(f"{medianaNum}")
