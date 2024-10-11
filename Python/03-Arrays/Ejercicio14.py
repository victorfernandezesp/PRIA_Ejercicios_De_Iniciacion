""" 
    14. Dado un número con más de 10 dígitos, suma los 3 primeros dígitos y los 3 últimos dígitos.

    @author Victor Fernandez España

"""

array = []


while True:
    numero = input("Introduce un número:    ")
    array = [int(digit) for digit in numero]
    if len(numero) >= 10:
        break

print(array)
suma = (
    array[0]
    + array[1]
    + array[2]
    + array[(len(array) - 1)]
    + array[(len(array) - 2)]
    + array[(len(array) - 3)]
)
print(f"{suma}")
