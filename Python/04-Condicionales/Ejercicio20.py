""" 
    20. Determina si un entero (mayor que 0 y menor que 10 000) al leerlo contiene la palabra cinco.


    @author Victor Fernandez España

"""

numero = int(input("Introduce un número entero mayor que 0 y menor que 10,000: "))

numeros_no_se_leen_como_cinco = [
    15,
    150,
    251,
    350,
    500,
    515,
    750,
    751,
    752,
    753,
    754,
    756,
    757,
    758,
    759,
    850,
    851,
    852,
    853,
    854,
    856,
    857,
    858,
    859,
    950,
    951,
    952,
    953,
    954,
    956,
    957,
    958,
    959,
]

if 0 < numero < 10000:
    numero_str = str(numero)

    if "5" in numero_str and numero not in numeros_no_se_leen_como_cinco:
        print("Sí.")
    else:
        print("No.")
else:
    print("Número fuera de rango.")
