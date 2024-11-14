"""
    10. Muestra en pantalla el número de ocurrencias de cada dígito en un número entero.
    Por ejemplo, para el número entero 116242320 imprimir que hay 2 unos, 3 doses, etc.

    @author Victor Fernandez España
"""

numero = 116242320
conteo = {}

for digito in str(numero):
    if digito in conteo:
        conteo[digito] += 1
    else:
        conteo[digito] = 1

for digito, cantidad in conteo.items():
    print(f"Hay {cantidad} {digito}{'s' if cantidad > 1 else ''}.")
