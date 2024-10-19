""" 
    16. Dadas dos series de tres enteros, comprueba si todos los enteros de la primera serie aparecen en alguno de los enteros de la segunda serie.



    @author Victor Fernandez España

"""

entero1 = int(input("Introduce un número:       "))
entero2 = int(input("Introduce un número:       "))
entero3 = int(input("Introduce un número:       "))
entero4 = int(input("Introduce un número:       "))
entero5 = int(input("Introduce un número:       "))
entero6 = int(input("Introduce un número:       "))

primero_en_segunda = entero1 == entero4 or entero1 == entero5 or entero1 == entero6
segundo_en_segunda = entero2 == entero4 or entero2 == entero5 or entero2 == entero6
tercero_en_segunda = entero3 == entero4 or entero3 == entero5 or entero3 == entero6

if primero_en_segunda and segundo_en_segunda and tercero_en_segunda:
    print("Sí.")
else:
    print("No.")
