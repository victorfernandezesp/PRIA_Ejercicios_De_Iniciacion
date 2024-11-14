""" 

    4. Crea una función que reciba un parámetro de entrada de tipo array, o lista, de tipo numérico y que devuelva un array, o lista, con la media y con otro array, o lista, con los números ordenados de mayor a menor. Ejecuta 3 llamadas de ejemplo de la función creada.


    @author Victor Fernandez España

"""


def listador(array: list):
    array.sort()
    media = sum(array) / len(array)
    return [media, array]

def main():
    
        print(listador([4, 5]))
        print(listador([5, 4]))
        print(listador([6, 6]))


if __name__ == "__main__":
    main()
