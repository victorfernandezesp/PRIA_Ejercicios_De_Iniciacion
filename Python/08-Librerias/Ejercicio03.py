""" 

    3. Usando librerías internas, abre y lee los siguientes archivos de texto: 1 y 2. Almacena cada texto en una variable de tipo cadena de caracteres o string. Luego, concatena las dos variables de tipo string en una nueva variable de tipo string denominada textos_concatenados. Por último, crea un nuevo fichero y escribe en él el contenido de textos_concatenados.


    @author Victor Fernandez España

"""

import os

ruta_texto1 = "C:/Escritorio/Pria/Python/08-Librerias/texto1.txt"
ruta_texto2 = "C:/Escritorio/Pria/Python/08-Librerias/texto2.txt"
ruta_texto3 = "C:/Escritorio/Pria/Python/08-Librerias/texto3.txt"

texto1 = open(ruta_texto1, "r")
texto2 = open(ruta_texto2, "r")
textos_concatenados = texto1.read() + texto2.read()
texto1.close()
texto2.close()

texto3 = open(ruta_texto3, "w")
texto3.write(textos_concatenados)
texto3.close()

print("Se ha creado un nuevo fichero con el contenido de los dos ficheros anteriores.")
print("El contenido del nuevo fichero es el siguiente:")

texto3 = open(ruta_texto3, "r")
print(texto3.read())
texto3.close()
