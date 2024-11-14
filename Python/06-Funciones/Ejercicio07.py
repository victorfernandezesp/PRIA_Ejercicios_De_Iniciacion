""" 

    7. Crea una función que reciba dos parámetros de entrada de tipo array, o lista, una de ellas de tipo string o cadena de caracteres y la otra de tipo numérico y que devuelva un array, o lista, donde se combine los dos array, o listas, alternativamente. Por ejemplo, la función devolverá ['hola', 3, 'qué', 6, 'tal', -4.5] si las entradas son ['hola', 'qué', 'tal'] y [3, 6, -4.5]. Ejecuta 3 llamadas de ejemplo de la función creada.





    @author Victor Fernandez España

"""


def combinar(array1: list, array2: list):
    array = []
    for i in range(len(array1)):
        array.append(array1[i])
        array.append(array2[i])
    return array


def main():

    print(combinar(["hola", "qué", "tal"], [3, 6, -4.5]))
    print(combinar(["uno", "dos", "tres"], [1, 2, 3]))
    print(combinar(["rojo", "verde", "azul"], [255, 255, 255]))


if __name__ == "__main__":
    main()
