""" 
    4. Crea un array/lista con cinco elementos y elimina el primer, tercer y último elemento. Por último, imprime de nuevo el array, o lista,.


    @author Victor Fernandez España

"""

array = [1, 2, 3, 4, 5]
array.pop(4)
array.pop(2)
array.pop(0)

print(f"El array final es: {array}")