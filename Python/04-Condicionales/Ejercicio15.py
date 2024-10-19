""" 
    15. Detecta la primera aparición de un entero a partir de una serie de cinco enteros devolviendo el índice con su posición.




    @author Victor Fernandez España

"""

entero1 = int(input("Introduce el número a buscar:       "))
entero2 = int(input("Introduce un número:       "))
entero3 = int(input("Introduce un número:       "))
entero4 = int(input("Introduce un número:       "))
entero5 = int(input("Introduce un número:       "))
entero6 = int(input("Introduce un número:       "))

array = [entero2, entero3, entero4, entero5, entero6]
if entero1 == array[0]:
    print(f"1")
elif entero1 == array[1]:
    print(f"2")
elif entero1 == array[2]:
    print(f"3")
elif entero1 == array[3]:
    print(f"4")
elif entero1 == array[4]:
    print(f"5")
else:
    print(f"No está el número.")
