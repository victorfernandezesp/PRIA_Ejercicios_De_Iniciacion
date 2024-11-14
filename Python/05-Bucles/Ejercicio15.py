"""
    15. Muestra la suma de los dígitos de 2n, siendo n un número natural.

    @author Victor Fernandez España
"""

n = 12

valor = str(2**n)
acumulador = 0
for i in valor:
    acumulador += int(i)

print(acumulador)
