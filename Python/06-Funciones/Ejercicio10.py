""" 

    10. Crea una función que reciba un parámetro de entrada de tipo numérico que tenga más de 10 dígitos (la función devolverá 0 si el número tiene 10 o menos dígitos) y que devuelva como salida los 5 dígitos consecutivos con mayor suma. Por ejemplo, la función devolverá 97798 si la entrada es 145436803497798443. Ejecuta 3 llamadas de ejemplo de la función creada.


    @author Victor Fernandez España

"""
def devuelveMayorSuma(num: int):
    num = str(num)
    if len(num) <= 10:
        return 0
    else:
        mayor = 0
        for i in range(len(num)-4):
            suma = int(num[i]) + int(num[i+1]) + int(num[i+2]) + int(num[i+3]) + int(num[i+4])
            if suma > mayor:
                mayor = suma
                resultado = num[i] + num[i+1] + num[i+2] + num[i+3] + num[i+4]
        return resultado


def main():
    print(devuelveMayorSuma(145436803497798443))
    print(devuelveMayorSuma(1454368034977984431))
    print(devuelveMayorSuma(14543680349779844312))



if __name__ == "__main__":
    main()
