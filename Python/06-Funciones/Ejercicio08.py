""" 

    8. Crea una función que reciba un parámetro de entrada de tipo numérico que sea mayor que 5 (la función devolverá 0 si el número es 5 o más pequeño) y que devuelva la suma de todos los números desde 1 hasta n sin contar con los elementos n - 1 ni n - 3. Por ejemplo, la función devolverá 24 si la entrada es 8. Ejecuta 3 llamadas de ejemplo de la función creada.






    @author Victor Fernandez España

"""
def sumador(num: int):
    if num <= 5:
        return 0
    else:
        suma = 0
        for i in range(1, num + 1):
            if i != num - 1 and i != num - 3:
                suma += i
        return suma


def main():
    print(sumador(8))
    print(sumador(9))
    print(sumador(10))

if __name__ == "__main__":
    main()
