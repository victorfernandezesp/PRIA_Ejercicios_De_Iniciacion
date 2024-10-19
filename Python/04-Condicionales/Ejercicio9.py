""" 
    9. Crea un programa que imprima por orden alfabético tres cadena de caracteres o strings dados y que imprima si son o no iguales dichos tres strings.



    @author Victor Fernandez España

"""

cadena1 = "Hola"
cadena2 = "Holaa"
cadena3 = "Holaaa"

arrayOrden = [cadena1, cadena2, cadena3]
arrayOrden.sort

print(f"Ordenado: {arrayOrden}")

if cadena1 == cadena2 == cadena3:
    print(f"Las cadenas SON iguales.")

else:
    print(f"Las cadenas NO son iguales.")
