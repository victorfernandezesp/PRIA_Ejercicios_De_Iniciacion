# ///////////////////
# BUCLES EN PYTHON //
# ///////////////////


"NO EXISTE DO-WHILE EN PYTHON"


# BUCLE CLÁSICO
print("BUCLE CLÁSICO")
for i in range(10):
    print(f"i:{i}\t", end='')
print("\n")

# Ejemplo visual: i:0	i:1	i:2	...

# BUCLE CLÁSICO CON LISTAS
print("BUCLE CLÁSICO CON LISTAS")
numeros = [-3.2, 5.3, 3.0, 1.0]
for i in range(len(numeros)):
    print(f"{numeros[i]}\t", end='')
print("\n")

# Ejemplo visual: -3.2	5.3	3.0	1.0	

# Es más común iterar directamente sobre los elementos:
print("BUCLE ITERANDO SOBRE ELEMENTOS DE LA LISTA")
for numero in numeros:
    print(f"{numero}\t", end='')
print("\n")

# Ejemplo visual: -3.2	5.3	3.0	1.0	

# BUCLE INVERSO
print("BUCLE INVERSO")
for i in range(5, -1, -1):
    print(f"i:{i}\t", end='')
print("\n")

# Ejemplo visual: i:5	i:4	i:3	i:2	...

# BUCLE ANIDADO
print("BUCLE ANIDADO")
for i in range(2):   # Ajustado a 2 para que sea más compacto
    print(f"i:{i}\t", end='')
    for j in range(2, 0, -1):
        print(f"j:{j}\t", end='')
        for k in range(2):
            print(f"k:{k}\t", end='')
    print()  # Nueva línea para mejorar visualización
print("\n")

# Ejemplo visual: i:0	j:2	k:0	k:1	j:1	k:0	k:1
#                i:1	j:2	k:0	k:1	j:1	k:0	k:1

# BUCLE CON VARIOS CONTADORES
print("BUCLE CON VARIOS CONTADORES")
for a, b in zip(range(5), range(5, 0, -1)):
    print(f"a:{a} b:{b}\t", end='')
print("\n")

# Ejemplo visual: a:0 b:5	a:1 b:4	a:2 b:3	...

# BUCLE ITERADOR
print("BUCLE ITERADOR")
colores = ["rojo", "verde", "azul", "amarillo"]
for color in colores:
    print(f"{color}\t", end='')
print("\n")

# Ejemplo visual: rojo	verde	azul	amarillo	

# BUCLE WHILE
print("BUCLE WHILE")
contador = 0
while contador <= 3:
    contador += 1
    print(f"Hola {contador}\t", end='')
print("\n")

# Ejemplo visual: Hola 1	Hola 2	Hola 3	Hola 4	

# EJEMPLO 1 (SUMATORIA)
print("EJEMPLO 1 (SUMATORIA)")
mi_lista = [-4.3, 2.0, -0.7, 1.5, 3.5]
suma = 0
for num in mi_lista:
    suma += num
    print(f"Suma parcial: {suma}")  # Visualizar suma parcial
print(f"La suma de todos los elementos de la lista es {suma}\n")

# Ejemplo visual: Suma parcial: -4.3, Suma parcial: -2.3, ...

# EJEMPLO 2 (PRODUCTO)
print("EJEMPLO 2 (PRODUCTO)")
lista_producto = [3.0, 2.0, -1.0, 1.0, 4.0]
producto = 1
for num in lista_producto:
    producto *= num
    print(f"Producto parcial: {producto}")  # Visualizar producto parcial
print(f"La multiplicación de todos los elementos de la lista es {producto}\n")

# Ejemplo visual: Producto parcial: 3.0, Producto parcial: 6.0, ...

# EJEMPLO 3 (PRIMO)
print("EJEMPLO 3 (PRIMO)")
lista_enteros = [4, 8, 15, 16, 23, 42]
numero_primo = -1

for num in lista_enteros:
    es_primo = True
    if num <= 1:
        es_primo = False
    else:
        for divisor in range(2, int(num ** 0.5) + 1):
            if num % divisor == 0:
                es_primo = False
                break
    if es_primo:
        numero_primo = num
        break

if numero_primo != -1:
    print(f"El primer número primo en la lista es {numero_primo}\n")
else:
    print("No hay números primos en la lista.\n")

# Ejemplo visual: 23 (el primer primo en la lista)

# EJEMPLO 4 (FACTORIAL)
print("EJEMPLO 4 (FACTORIAL)")
numero = 5
factorial = 1
for i in range(1, numero + 1):
    factorial *= i
    print(f"Factorial parcial de {i} es {factorial}")  # Visualizar factorial parcial
print(f"El factorial de {numero} es {factorial}.\n")

# Ejemplo visual: Factorial parcial de 1 es 1, Factorial parcial de 2 es 2, ...

# EJEMPLO 5 (CREAR LISTAS CON BUCLES)
print("EJEMPLO 5 (CREAR LISTAS CON BUCLES)")
cuadrados = [x**2 for x in range(10)]
print(f"Cuadrados: {cuadrados[:3]} ... {cuadrados[-3:]}")  # Visualizar los primeros y últimos elementos
print("\n")

# Ejemplo visual: Cuadrados: [0, 1, 4] ... [49, 64, 81]
