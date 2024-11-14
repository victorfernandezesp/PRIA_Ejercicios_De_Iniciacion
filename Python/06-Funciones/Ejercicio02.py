""" 

    2. Crea una función que reciba dos parámetros de entrada de tipo númerico y que devuelva el máximo. Ejecuta 3 llamadas de ejemplo de la función creada.



    @author Victor Fernandez España

"""


def maximo(num1, num2):
    return num1 if num1 > num2 else num2


def main():

    print(maximo(4, 5))
    print(maximo(5, 4))
    print(maximo(6, 6))


if __name__ == "__main__":
    main()
