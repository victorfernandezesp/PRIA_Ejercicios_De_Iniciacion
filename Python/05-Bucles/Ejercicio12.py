"""
    12. Dado un string o cadena de caracteres, muestra solo sus consonantes.

    @author Victor Fernandez España
"""

cadena = "Esto es un enunciado"
vocales = "AEIOUÁÉÍÓÚÜaeiouáéíóúü"
concatenado = ""
for i in cadena:
    if i not in vocales:
        concatenado += i

print(concatenado)