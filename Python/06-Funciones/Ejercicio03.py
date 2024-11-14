""" 

    3. Crea una función que reciba dos parámetros de entrada de tipo númerico y que devuelva un array, o lista, con el máximo, el mínimo y la media de esos dos números. Ejecuta 3 llamadas de ejemplo de la función creada.




    @author Victor Fernandez España

"""


def listador(num1: int, num2: int):
    array = []
    array.append(num1)
    array.append(num2)
    array.append((num1 + num2) / 2)
    array.sort()
    return array

def main():

    print(listador(4, 5))
    print(listador(5, 4))
    print(listador(6, 6))


if __name__ == "__main__":
    main()
