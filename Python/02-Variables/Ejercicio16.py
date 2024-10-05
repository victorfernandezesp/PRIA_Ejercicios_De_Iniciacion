""" 
    16. Dado un entero, indica con un 0 si el número es par y con un 1 si el número es impar.


    @author Victor Fernandez España

"""

# Sin pasar como parámetros
print("\n\n\n\n\n")
print("Sin pasar como parámetros")


numero1 = 2
parimpar = numero1%2
print("Es: ", parimpar)
print("------------------------------------------------------------------------" )

numero1 = 7
parimpar = numero1%2
print("Es: ", parimpar)
print("------------------------------------------------------------------------" )

numero1 = 10
parimpar = numero1%2
print("Es: ", parimpar)
print("------------------------------------------------------------------------" )



# Pasando como parámetros

print("Pasando como parámetros")
numero1 = int(input("Introduce el número 1:     "))
parimpar = numero1%2
print("Es: ", parimpar)
print("------------------------------------------------------------------------" )