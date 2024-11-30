""" 

    9. Crea una función que reciba un parámetro de entrada de tipo array/lista, con identificador grupos, de tamaño 3 cuyos elementos sean de tipo array/lista de clase Estudiante (realizado en ejercicio 05). La función tiene que devolver el índice del array/lista grupos cuyo promedio de notas del grupo de estudiantes sea el más alto. Ejecuta 1 llamada de ejemplo de la función creada.

    Por ejemplo, hay tres grupos de Bachillerato con 25 alumnos cada uno. Cada grupo será un array/lista de 25 estudiantes (25 objetos/instancias de la clase Estudiante) que se añadirá al array/lista grupos inicialmente vacío. Cada estudiante tiene su media final, pero lo que queremos es la media de todo ese grupo de estudiantes y compararlos con los otros grupos. Lo que buscamos finalmente es conocer qué grupo de bachillerato tiene los alumnos con mejor promedio de nota. Si se va a usar este ejemplo en el ejercicio, no es necesario tantos alumnos (5 por grupo sería más que suficiente).


    @author Victor Fernandez España

"""
from Ejercicio05 import Estudiante
from math import pi


from Ejercicio05 import Estudiante

def indice_grupo_promedio(grupos: list):
    promedios = [
        sum(estudiante.mediaNotas() for estudiante in grupo) / len(grupo)
        for grupo in grupos
    ]
    return promedios.index(max(promedios))


grupo1 = [
    Estudiante("Victor", [10, 20, 30]),
    Estudiante("Pepe", [15, 25, 35]),
    Estudiante("Juan", [20, 30, 40]),
    Estudiante("Ana", [25, 35, 45]),
    Estudiante("Luis", [30, 40, 50]),
]

grupo2 = [
    Estudiante("Marta", [50, 60, 70]),
    Estudiante("Pablo", [55, 65, 75]),
    Estudiante("Sara", [60, 70, 80]),
    Estudiante("Lara", [65, 75, 85]),
    Estudiante("David", [70, 80, 90]),
]

grupo3 = [
    Estudiante("Julia", [80, 90, 100]),
    Estudiante("Sofia", [85, 95, 105]),
    Estudiante("Mario", [90, 100, 110]),
    Estudiante("Paula", [95, 105, 115]),
    Estudiante("Alvaro", [100, 110, 120]),
]

grupos = [grupo1, grupo2, grupo3]
indice_mejor_grupo = indice_grupo_promedio(grupos)
print(f"El índice del grupo con el mejor promedio es: {indice_mejor_grupo}")

