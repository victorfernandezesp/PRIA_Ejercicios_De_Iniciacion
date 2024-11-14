""" 

    6. Crea una función que actúe como una calculadora simple. Para ello, la función recibirá tres parámetros de entrada, dos de tipo numérico para los valores y un string o cadena de caracteres para la operación (+, -, * o /). La función devolverá el resultado de la operación elegida entre esos dos números. Ejecuta 3 llamadas de ejemplo de la función creada.




    @author Victor Fernandez España

"""

def calculadora(num1: int, num2: int, operacion: str):
    if operacion == "+":
        return num1 + num2
    elif operacion == "-":
        return num1 - num2
    elif operacion == "*":
        return num1 * num2
    elif operacion == "/":
        return num1 / num2
    else:
        return "Operación no válida"



def main():
    
        print(calculadora(4, 5, "+"))
        print(calculadora(5, 4, "-"))
        print(calculadora(6, 6, "*"))



if __name__ == "__main__":
    main()
