""" 

    9. Crea una función que reciba un parámetro de entrada de tipo array, o lista, de tipo string o cadena de caracteres y que imprima los strings dentro de un rectángulo. Por ejemplo, para el array, o lista, ['Me', 'gusta', 'la', 'pizza', 'margherita'] se imprimirá el siguiente rectángulo:

    **************
    * Me         *
    * gusta      *
    * la         *
    * pizza      *
    * margherita *
    **************
    Ejecuta 3 llamadas de ejemplo de la función creada.






    @author Victor Fernandez España

"""
def imprimeStrings(array: list):
    maximo = len(max(array, key=len))
    print("*" * (maximo + 2))
    for i in array:
        print("* " + i + " " * (maximo - len(i)) + " *")
    print("*" * (maximo + 2))


def main():
    imprimeStrings(['Me', 'gusta', 'la', 'pizza', 'margherita'])
    imprimeStrings(['Me', 'gusta', 'la', 'pizza'])
    imprimeStrings(['Me', 'gusta', 'la', 'pizza', 'margherita', 'SIN', 'piña'])


if __name__ == "__main__":
    main()
