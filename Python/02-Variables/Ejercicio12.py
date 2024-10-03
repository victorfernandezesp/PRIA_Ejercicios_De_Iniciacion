""" 
    12. Realiza un conversor de Fahrenheit a Celsius.


    @author Victor Fernandez España

"""

# Sin pasar como parámetros
print("\n\n\n\n\n")
print("Sin pasar como parámetros")
numero1 = 68
numero2 = 13
numero3 = -145.6
print(numero1, "ºF = ", ((5/9)*(numero1-32)),"ºC" )
print(numero2, "ºF = ", ((5/9)*(numero2-32)),"ºC" )
print(numero3, "ºF = ", ((5/9)*(numero3-32)),"ºC" )
print("------------------------------------------------------------------------" )

# Pasando como parámetros

print("Pasando como parámetros")
numero1 = int(input("Introduce los grados Fahrenheit :     "))
print(numero1, "ºF = ", ((5/9)*(numero1-32)),"ºC" )
print("------------------------------------------------------------------------" )