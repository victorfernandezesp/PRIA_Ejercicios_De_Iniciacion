""" 
    13. Calcula el área y el perímetro de un rectángulo dado sus lados.

    @author Victor Fernandez España

"""

# Sin pasar como parámetros
print("\n\n\n\n\n")
print("Sin pasar como parámetros")
numero1 = 3
numero2 = 2
print("Área: ", (numero1*numero2))
print("Perímetro: ", ((numero1*2) + (numero2*2)))
print("------------------------------------------------------------------------" )
numero1 = 2
numero2 = 4
print("Área: ", (numero1*numero2))
print("Perímetro: ", ((numero1*2) + (numero2*2)))
print("------------------------------------------------------------------------" )
numero1 = 4
numero2 = 5
print("Área: ", (numero1*numero2))
print("Perímetro: ", ((numero1*2) + (numero2*2)))
print("------------------------------------------------------------------------" )

# Pasando como parámetros

print("Pasando como parámetros")
numero1 = int(input("Introduce la base:     "))
numero2 = int(input("Introduce la altura:   "))
print("Área: ", (numero1*numero2))
print("Perímetro: ", (numero1*2 +numero2*2))
print("------------------------------------------------------------------------" )