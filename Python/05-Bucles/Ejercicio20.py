"""
    20. Imprime la suma de enteros recibidos pero ignorando los subconjuntos que empiecen por 6 y terminen en 7.

    @author Victor Fernandez España
"""

entrada = input("Introduce los números separados por espacios: ")

numeros = list(map(int, entrada.split()))

suma_total = 0
en_subconjunto = False

for num in numeros:
    if num == 6:
        en_subconjunto = True  
    elif num == 7 and en_subconjunto:
        en_subconjunto = False  
    elif not en_subconjunto:
        suma_total += num 

print(suma_total)
