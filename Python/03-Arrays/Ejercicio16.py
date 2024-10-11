""" 
    16. Dada una serie de palabras, ordénalas alfabéticamente al revés (de z a a). A continuación, muestra el resultado final exceptuando la primera palabra y las tres últimas palabras.


    @author Victor Fernandez España

"""

array = []
palabra = input("Escribe la palabra:     ")
array.append(palabra)
palabra = input("Escribe la palabra:     ")
array.append(palabra)
palabra = input("Escribe la palabra:     ")
array.append(palabra)
palabra = input("Escribe la palabra:     ")
array.append(palabra)
palabra = input("Escribe la palabra:     ")
array.append(palabra)
palabra = input("Escribe la palabra:     ")
array.append(palabra)
palabra = input("Escribe la palabra:     ")
array.append(palabra)

array.sort()
array.reverse()
array.pop(0)
array.pop()
array.pop()
array.pop()
print(f"{array}")
