""" 
    9. Imprime los números que sean divisibles por 7 y por 5 entre el rango 1500 y 2700 (ambos incluidos).

    @author Victor Fernandez España

"""

for i in range(1500, 2700 + 1):
    if i % 5 == 0 and i % 7 == 0:
        print(f"{i}")
