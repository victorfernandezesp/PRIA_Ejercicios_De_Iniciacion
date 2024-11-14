"""
    18. Devuelve el entero más grande adyacente a un cero.

    @author Victor Fernandez España
"""

numeros = [1, 5, 3, 0, 2, 7, 0, 8, 9, 1, 1]

max_adjacente = None

for i in range(len(numeros)):
    if numeros[i] == 0:
        if i > 0 and (max_adjacente is None or numeros[i - 1] > max_adjacente):
            max_adjacente = numeros[i - 1]
        if i < len(numeros) - 1 and (max_adjacente is None or numeros[i + 1] > max_adjacente):
            max_adjacente = numeros[i + 1]

print(max_adjacente)
