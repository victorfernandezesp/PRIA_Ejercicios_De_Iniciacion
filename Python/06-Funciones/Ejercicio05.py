""" 

    5. Crea una función que reciba un parámetro de entrada de tipo numérico y que devuelva un array, o lista, con todos los dígitos de ese número. Por ejemplo, la función devolverá [3, 4, 4] si la entrada es 344. Ejecuta 3 llamadas de ejemplo de la función creada.



    @author Victor Fernandez España

"""

def listador(num: int):
    lista = []
    for i in str(num):
        lista.append(int(i))
    return lista


def main():
    print(listador(344))
    print(listador(345))
    print(listador(346))


if __name__ == "__main__":
    main()
