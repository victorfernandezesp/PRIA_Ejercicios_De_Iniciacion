""" 
    18. Imprime GNU si el número recibido es impar.


    @author Victor Fernandez España

"""

# Sin pasar como parámetros
print("\n\n\n\n\n")
print("Sin pasar como parámetros")


numero1 = 5
parimpar1 = numero1 % 2
print("GNU" * parimpar1)
print("------------------------------------------------------------------------")

numero2 = 4
parimpar2 = numero2 % 2 
print("GNU" * parimpar2)
print("------------------------------------------------------------------------")

numero3 = 11
parimpar3 = numero3 % 2 
print("GNU" * parimpar3)
print("------------------------------------------------------------------------")


# Pasando como parámetros

print("Pasando como parámetros")

numero1 = int(input("Escribe un numero:     "))
parimpar1 = numero1 % 2 
print("GNU" * parimpar1)
print("------------------------------------------------------------------------")
