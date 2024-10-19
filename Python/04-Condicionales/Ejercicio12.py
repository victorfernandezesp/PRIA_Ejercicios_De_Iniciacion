""" 
    12. Dado tres enteros, devuelve verdadero si no aparece ni un 1 y ni un 3.



    @author Victor Fernandez España

"""

entero1 = int(input("Introduce un número:       "))
entero2 = int(input("Introduce un número:       "))
entero3 = int(input("Introduce un número:       "))

noAparecen = [1, 3]

if entero1 not in noAparecen and entero2 not in noAparecen and entero3 not in noAparecen:
    print(f"True")

else:
    print(f"False")
