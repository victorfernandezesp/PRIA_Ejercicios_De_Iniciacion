"""
    16. Determina si los enteros dados están aumentando constantemente.

    @author Victor Fernandez España
"""

# numeros = [-3, 2, 4, 6]
numeros = [3, 5, 2]
ultimoNum = numeros[0]
switch = "Si."

for i in range(len(numeros)):
    if i == 0:
        pass
    else:
        if i < ultimoNum:
            switch = "No."
            break
        else:
            ultimoNum = i

print(f"{switch}")
