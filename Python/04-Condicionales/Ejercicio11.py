""" 
    11. Dado dos enteros, calcula la suma. Si el resultado está entre 10 y 19 (ambos incluídos), imprime 20. Si no, imprime la suma.



    @author Victor Fernandez España

"""

entero1 = int(input("Introduce un número:       "))
entero2 = int(input("Introduce un número:       "))

resultado = entero1 + entero2

if 10<=resultado<=19:
    print(f"20.")

else:
    print(f"{resultado}.")
