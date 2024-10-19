""" 
    14. Elimina todas las vocales dada una cadena, o string, de cinco caracteres.



    @author Victor Fernandez España

"""

cadena = input("Introduce una cadena de 5 caracteres:       ")
vocales = "AEIOUaeiouáéíóúÁÉÍÓÚ"


if len(cadena) != 5:
    print(f"Tiene que tener 5 caracteres.")
else:
    if cadena[0] in vocales:
        cadena = cadena.replace(cadena[0], "", 1)
    if len(cadena) > 1 and cadena[1] in vocales:
        cadena = cadena.replace(cadena[1], "", 1)
    if len(cadena) > 2 and cadena[2] in vocales:
        cadena = cadena.replace(cadena[2], "", 1)
    if len(cadena) > 3 and cadena[3] in vocales:
        cadena = cadena.replace(cadena[3], "", 1)
    if len(cadena) > 4 and cadena[4] in vocales:
        cadena = cadena.replace(cadena[4], "", 1)

    print(f"Cadena sin vocales: {cadena}")
