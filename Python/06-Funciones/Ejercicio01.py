""" 
    1. Crea una función que reciba un parámetro de entrada de tipo entero y que devuelva un booleano con valor true si el número es par y false si es impar. Ejecuta 3 llamadas de ejemplo de la función creada.




    @author Victor Fernandez España

"""


def esPar(num):
    return num % 2 == 0


def main():

    print(esPar(4))
    print(esPar(5))
    print(esPar(6))


if __name__ == "__main__":
    main()
