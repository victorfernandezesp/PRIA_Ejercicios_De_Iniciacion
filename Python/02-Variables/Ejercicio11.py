""" 
    11. Dado tres enteros, súmalos e imprime el resultado.

    @author Victor Fernandez España

"""

# Sin pasar como parámetros
print("\n\n\n\n\n")
print("Sin pasar como parámetros")
numero1 = 3
numero2 = 7
numero3 = 5

suma = (numero1+numero2+numero3)
print(numero1, "+", numero2, "+", numero3, "=", suma )
print("------------------------------------------------------------------------" )

numero1 = -5
numero2 = 4
numero3 = 8
suma = (numero1+numero2+numero3)
print(numero1, "+", numero2, "+", numero3, "=", suma )
print("------------------------------------------------------------------------" )

numero1 = 10
numero2 = -12
numero3 = -50
suma = (numero1+numero2+numero3)
print(numero1, "+", numero2, "+", numero3, "=", suma )
print("------------------------------------------------------------------------" )


# Pasando como parámetros

print("Pasando como parámetros")
numero1 = int(input("Introduce el número 1:     "))
numero2 = int(input("Introduce el número 2:     "))
numero3 = int(input("Introduce el número 3:     "))
suma = (numero1+numero2+numero3)
print(numero1, "+", numero2, "+", numero3, "=", suma )
print("------------------------------------------------------------------------" )