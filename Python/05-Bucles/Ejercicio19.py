"""
    19. Muestra los dígitos, ordenados de menor a mayor, que aparecen exactamente tres veces.

    @author Victor Fernandez España
"""

numero = "13533782212888"

conteo = {}
for digito in numero:
    if digito in conteo:
        conteo[digito] += 1
    else:
        conteo[digito] = 1

diez_digitos_tres_veces = [int(digito) for digito, count in conteo.items() if count == 3]

diez_digitos_tres_veces.sort()

print(" ".join(map(str, diez_digitos_tres_veces)))
