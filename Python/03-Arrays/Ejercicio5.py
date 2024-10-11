""" 
    5. Crea un array/lista con cinco elementos e inserta en el primer índice, tercero y último tres números. Por último, imprime de nuevo el array, o lista,.

    @author Victor Fernandez España

"""

array = [1, 2, 3, 4, 5]
array.insert(1, 8)
array.insert(3, 7)
array.reverse()
array.insert(0, 6)
array.reverse()

print(f"El array final es: {array}")