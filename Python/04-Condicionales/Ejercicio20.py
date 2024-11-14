""" 
    20. Determina si un entero (mayor que 0 y menor que 10 000) al leerlo contiene la palabra cinco.


    @author Victor Fernandez España

"""

# numero = int(input("Introduce un número entero mayor que 0 y menor que 10,000: "))
numero = 850

if (5000 <= numero < 6000) or (numero % 5 == 0 and numero % 2 != 0 and (numero - 15) % 100 != 0):
    print("Si.")
else:
    print("No.")
