"""
    13. Dado una serie de enteros, devuelve verdadero si no aparece ni un 1 y ni un 3.



    @author Victor Fernandez España
"""

numeros = [-1, 4, 1, -3, 9]
interruptor = True
betados = [1, 3]
for i in numeros:
    if i in betados:
        interruptor = False

print(f"{interruptor}")
