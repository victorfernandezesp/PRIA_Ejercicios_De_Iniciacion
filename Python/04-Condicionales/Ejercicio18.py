""" 
    18. Dados dos enteros positivos, imprime el valor más cercano a 21 sin sobrepasarse. Imprime 0 si los dos enteros son mayores que 21.


    @author Victor Fernandez España

"""

numero1 = int(input("Introduce un número:       "))
numero2 = int(input("Introduce un número:       "))


numeros = [numero1, numero2]

if max(numeros)<=21:
    print(f"{max(numeros)}")
elif min(numeros)<=21:
    print(f"{min(numeros)}")
else:
    print(f"0")