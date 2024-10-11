""" 
    15. Dada una serie de palabras, ordénalas alfabéticamente.

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

array.sort()
print(f"{array}")