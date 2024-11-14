"""
    21. Imprime los enteros recibidos reorganizados de tal manera que después de un 3 haya un 4. 
        Los treses no pueden cambiar de posición.

    @author Victor Fernandez España
"""

entrada = input("Introduce los números separados por espacios: ")

numeros = list(map(int, entrada.split()))

resultado = []
cuatros = 0  

for num in numeros:
    if num == 3:
        resultado.append(num) 
        resultado.append(4)   
        cuatros += 1 
    elif num == 4:
        if cuatros > 0:  
            continue 
    else:
        resultado.append(num) 

resultado = [x for x in resultado if x != 4 or (x == 4 and cuatros > 0)]

print(" ".join(map(str, resultado)))
