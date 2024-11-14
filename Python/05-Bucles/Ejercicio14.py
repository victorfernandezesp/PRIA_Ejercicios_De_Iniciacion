"""
    14. Dado una serie de enteros, devuelve verdadero si aparece alguna vez 3 enteros impares consecutivos.


    @author Victor Fernandez España
"""

# numeros = [9, 7, 2, 1, 1, 2]
numeros = [3, 5, 3, 4]

interruptor = False
for i in range(len(numeros) - 2):
    if numeros[i] % 2 == 1 and numeros[i + 1] % 2 == 1 and numeros[i + 2] % 2 == 1:
        interruptor = True
        break

print(f"{interruptor}")
