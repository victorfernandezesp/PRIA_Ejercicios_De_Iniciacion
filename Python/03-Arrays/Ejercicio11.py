""" 
    11. A partir de 5 números, muestra aquellos que no sean el mayor ni el menor y ordenados de mayor a menor.

    @author Victor Fernandez España

"""
array = []
numero = int(input("Introduce un número:    "))
array.append(numero)
numero = int(input("Introduce un número:    "))
array.append(numero)
numero = int(input("Introduce un número:    "))
array.append(numero)
numero = int(input("Introduce un número:    "))
array.append(numero)
numero = int(input("Introduce un número:    "))
array.append(numero)

print(f"Array sin modificar:    {array}")
array.sort
array.pop()
array.reverse()
array.pop()
array.reverse()
array.reverse()

print(f"Array modificado:       {array}")