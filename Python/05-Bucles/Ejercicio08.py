""" 
    8. Imprime en pantalla, solo usando un bucle, el siguiente patrón:

    @author Victor Fernandez España

"""

nuemerodado = 9

for i in range(nuemerodado + 1):
    print(f"{str(i)*i}")

caracter = "*"
for j in range(6):
    print(f"{caracter*j}")

for k in range(5, 0, -1):
    print(f"{caracter*k}")
