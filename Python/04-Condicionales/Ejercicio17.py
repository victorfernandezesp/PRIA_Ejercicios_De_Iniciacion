""" 
    17. Convierte de centímetros a metros y vicerversa.


    @author Victor Fernandez España

"""

numero1 = float(input("Introduce un número:       "))
medida2 = input("Introduce la medida (cm/m):       ")

medidas = ["cm", "m"]
if medida2 not in medidas:
    print(f"La medida introducida no es correcta.")
else:
    if medida2 == medidas[0]:
        numero1 *= 0.01
        print(f"La conversión da: {numero1}m")
    else:
        numero1 *= 100
        print(f"La conversión da: {numero1}cm")
